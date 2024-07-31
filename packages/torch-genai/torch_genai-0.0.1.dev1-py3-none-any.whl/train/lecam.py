import torch
import torch.nn as nn
import torch.nn.functional as F


class LeCAM_EMA:
    def __init__(self, init=0.0, decay=0.999):
        self.logits_real_ema = init
        self.logits_fake_ema = init
        self.decay = decay

    def update(self, logits_real, logits_fake):
        self.logits_real_ema = self.logits_real_ema * self.decay + torch.mean(
            logits_real
        ).item() * (1 - self.decay)
        self.logits_fake_ema = self.logits_fake_ema * self.decay + torch.mean(
            logits_fake
        ).item() * (1 - self.decay)


def lecam_reg(real_pred, fake_pred, lecam_ema):
    reg = torch.mean(F.relu(real_pred - lecam_ema.logits_fake_ema).pow(2)) + torch.mean(
        F.relu(lecam_ema.logits_real_ema - fake_pred).pow(2)
    )
    return reg


if __name__ == "__main__":
    from hiq import deterministic

    ema_tracker = LeCAM_EMA()

    # 真实和生成 logits 示例
    logits_real = torch.randn(32)  # 模拟批量大小为 32 的真实 logits
    logits_fake = torch.randn(32)  # 模拟批量大小为 32 的生成 logits

    # 更新 EMA 值
    ema_tracker.update(logits_real, logits_fake)

    print(f"Updated logits_real_ema: {ema_tracker.logits_real_ema}")
    print(f"Updated logits_fake_ema: {ema_tracker.logits_fake_ema}")

"""
`LeCAM_EMA` 是一个用于维护指数移动平均值 (Exponential Moving Average, EMA) 的类，专门用于 GAN (生成对抗网络) 中的 LeCAM 方法。
EMA 是一种平滑技术，可以用来跟踪变量的平均值，使得最新的数据点对平均值的影响更大。

### 详细解释

1. **构造函数 `__init__`**:
    - `init=0.0`: 初始化真实和生成 logits 的 EMA 值。
    - `decay=0.999`: 衰减因子，控制 EMA 的平滑程度。衰减因子越接近 1，EMA 更新越慢，历史数据的权重越大。

```python
class LeCAM_EMA(object):
    def __init__(self, init=0.0, decay=0.999):
        self.logits_real_ema = init
        self.logits_fake_ema = init
        self.decay = decay
```

2. **更新函数 `update`**:
    - 更新真实和生成 logits 的 EMA 值。
    - `logits_real` 和 `logits_fake` 是从判别器得到的 logits 张量。
    - `torch.mean(logits_real).item()`: 计算真实 logits 的平均值，并将其转换为标量。
    - EMA 更新公式：
      \[
      \text{EMA}_{\text{new}} = \text{EMA}_{\text{old}} \times \text{decay} + \text{value} \times (1 - \text{decay})
      \]
    - 公式中，`decay` 控制了新值对 EMA 的贡献大小。

```python
    def update(self, logits_real, logits_fake):
        self.logits_real_ema = self.logits_real_ema * self.decay + torch.mean(
            logits_real
        ).item() * (1 - self.decay)
        self.logits_fake_ema = self.logits_fake_ema * self.decay + torch.mean(
            logits_fake
        ).item() * (1 - self.decay)
```

### 用途

1. **平滑真实和生成 logits**:
    - 通过 EMA，可以获得更稳定的真实和生成 logits 的估计值，减少波动。
    - 在 GAN 中，这种平滑有助于更稳定的训练过程。

2. **LeCAM 方法**:
    - LeCAM (Least Squares GAN with EMA Classifier Mean) 是一种改进 GAN 稳定性的技术，通过使用 EMA 计算分类器的均值来调整生成器的训练目标。
    - 该类实现了 LeCAM 所需的 EMA 计算。

### 示例

假设你有 GAN 的真实和生成 logits，可以如下更新 EMA 值：

```python
ema_tracker = LeCAM_EMA()

# 真实和生成 logits 示例
logits_real = torch.randn(32)  # 模拟批量大小为 32 的真实 logits
logits_fake = torch.randn(32)  # 模拟批量大小为 32 的生成 logits

# 更新 EMA 值
ema_tracker.update(logits_real, logits_fake)

print(f"Updated logits_real_ema: {ema_tracker.logits_real_ema}")
print(f"Updated logits_fake_ema: {ema_tracker.logits_fake_ema}")
```

通过以上代码，可以看到真实和生成 logits 的 EMA 值随着每次更新逐渐变化并趋于稳定。
"""
