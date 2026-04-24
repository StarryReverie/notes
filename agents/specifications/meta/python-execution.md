# Python 脚本执行环境规范

本文件定义 Agent 调用 `agents/scripts/` 下 Python 脚本时的执行环境选择与依赖处理规则。

## 执行环境选择

按以下优先级尝试执行 Python 脚本：

1. NixOS 环境下，使用 `flake.nix` 中提供的 Python
2. Windows 或其他环境下，直接使用系统 `python`
3. 若 `python` 不可用，尝试 `uv run python`

## 依赖处理

- `agents/scripts/requirements.txt` 声明所有 Python 依赖
- Agent 不得自动执行 `pip install` 全局安装依赖，因为会污染系统环境
- 当脚本因缺少依赖而失败时，Agent 应告知用户缺失的依赖包名，由用户决定如何安装（如 `uv pip install`、`pip install --user`、加入 `flake.nix` 等）

## 合规判定

以下情况判定为不合规：

- Agent 未经用户确认自动执行 `pip install`（全局或用户级）
- Agent 在已知 `python` 不可用时未尝试 `uv run python`
- 脚本新增了依赖但未更新 `requirements.txt`
