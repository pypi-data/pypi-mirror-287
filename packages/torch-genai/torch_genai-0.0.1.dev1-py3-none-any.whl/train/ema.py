"""
定义了一个名为 LitEma 的 PyTorch 模块，用于实现指数移动平均（EMA，Exponential Moving Average）模型参数更新的功能。
EMA 是一种平滑技术，通过对模型参数进行加权平均，随着时间推移赋予新参数更少的权重，以此来平滑参数的更新，从而提高模型的稳定性和泛化能力。

Refer to
https://github.com/Stability-AI/stablediffusion/blob/main/ldm/modules/ema.py
"""


import torch
from torch import nn


class LitEma(nn.Module):
    def __init__(self, model, decay=0.999, use_num_upates=False):
        super().__init__()
        if decay < 0.0 or decay > 1.0:
            raise ValueError("Decay must be between 0 and 1")

        self.m_name2s_name = {}
        self.register_buffer("decay", torch.tensor(decay, dtype=torch.float32))
        self.register_buffer(
            "num_updates",
            torch.tensor(0, dtype=torch.int)
            if use_num_upates
            else torch.tensor(-1, dtype=torch.int),
        )

        for name, p in model.named_parameters():
            if p.requires_grad:
                # remove as '.'-character is not allowed in buffers
                s_name = name.replace(".", "")
                self.m_name2s_name.update({name: s_name})
                self.register_buffer(s_name, p.clone().detach().data)

        self.collected_params = []

    def reset_num_updates(self):
        del self.num_updates
        self.register_buffer("num_updates", torch.tensor(0, dtype=torch.int))

    def forward(self, model):
        decay = self.decay

        if self.num_updates >= 0:
            self.num_updates += 1
            decay = min(self.decay, (1 + self.num_updates) / (10 + self.num_updates))

        one_minus_decay = 1.0 - decay

        with torch.no_grad():
            m_param = dict(model.named_parameters())
            shadow_params = dict(self.named_buffers())

            for key in m_param:
                if m_param[key].requires_grad:
                    sname = self.m_name2s_name[key]
                    shadow_params[sname] = shadow_params[sname].type_as(m_param[key])
                    shadow_params[sname].sub_(
                        one_minus_decay * (shadow_params[sname] - m_param[key])
                    )
                else:
                    assert not key in self.m_name2s_name

    def copy_to(self, model):
        m_param = dict(model.named_parameters())
        shadow_params = dict(self.named_buffers())
        for key in m_param:
            if m_param[key].requires_grad:
                m_param[key].data.copy_(shadow_params[self.m_name2s_name[key]].data)
            else:
                assert not key in self.m_name2s_name

    def store(self, parameters):
        """
        Save the current parameters for restoring later.
        Args:
          parameters: Iterable of `torch.nn.Parameter`; the parameters to be
            temporarily stored.
        """
        self.collected_params = [param.clone() for param in parameters]

    def restore(self, parameters):
        """
        Restore the parameters stored with the `store` method.
        Useful to validate the model with EMA parameters without affecting the
        original optimization process. Store the parameters before the
        `copy_to` method. After validation (or model saving), use this to
        restore the former parameters.
        Args:
          parameters: Iterable of `torch.nn.Parameter`; the parameters to be
            updated with the stored parameters.
        """
        for c_param, param in zip(self.collected_params, parameters):
            param.data.copy_(c_param.data)


if __name__ == "__main__":
    import torch
    import torch.nn as nn
    import torch.optim as optim

    # 定义一个简单的模型
    class SimpleModel(nn.Module):
        def __init__(self):
            super(SimpleModel, self).__init__()
            self.fc = nn.Linear(10, 1)

        def forward(self, x):
            return self.fc(x)

    # 初始化模型和EMA模块
    model = SimpleModel()
    ema = LitEma(model, decay=0.999, use_num_upates=True)

    # 定义损失函数和优化器
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # 创建一些虚拟数据
    inputs = torch.randn(100, 10)
    targets = torch.randn(100, 1)

    # 训练过程
    num_epochs = 10
    for epoch in range(num_epochs):
        for i in range(100):
            # 前向传播
            outputs = model(inputs[i])
            loss = criterion(outputs, targets[i])

            # 反向传播和优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 更新EMA参数
            ema(model)

        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

    # 评估过程
    ema.copy_to(model)  # 使用EMA参数进行评估
    # 在这里进行模型评估，例如计算验证集的损失或准确率
    # 评估完成后，可以将原始参数恢复
    # ema.restore(model.parameters())  # 如果需要恢复原始参数

    # 保存模型
    torch.save(model.state_dict(), "model_with_ema.pth")

    # 载入模型
    model_loaded = SimpleModel()
    model_loaded.load_state_dict(torch.load("model_with_ema.pth"))

    # 将EMA参数复制到载入的模型中
    ema.copy_to(model_loaded)
    # 在这里可以继续使用载入的模型进行推理或进一步训练

    print("Model trained and saved with EMA parameters.")
