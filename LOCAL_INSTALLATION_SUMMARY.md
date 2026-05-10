# CLIPasso 本地安装问题总结

## 当前遇到的问题

### 1. 系统权限限制
```
PermissionError: [WinError 5] 拒绝访问: 'E:\Python3.7.0\Lib\site-packages\numpy'
```
系统Python目录(E:\Python3.7.0)受权限保护，普通用户无法直接安装包。

### 2. 包版本冲突
- 项目需要：torch==1.7.1, torchvision==0.8.2, numpy==1.19.2
- Python 3.7.0环境下，某些最新包的依赖要求无法满足
- scikit-image需要numpy>=1.22，但torchvision==0.8.2需要numpy<1.20

### 3. 大文件下载缓慢
- PyTorch + CUDA版本约2GB，下载经常超时
- 清华镜像源不包含所有版本

## 已成功安装的部分
✅ torch==1.7.1 (CPU版本)

## 推荐的解决方案

### 方案A：使用管理员权限安装（推荐）

重新以管理员身份打开PowerShell，然后：

```powershell
# 升级pip
python -m pip install --upgrade pip

# 安装PyTorch (CPU版本，避免CUDA兼容问题)
python -m pip install torch==1.7.1 torchvision==0.8.2

# 安装其他依赖
python -m pip install numpy==1.19.5 pillow matplotlib tqdm pandas
python -m pip install scikit-image==0.18.3 scipy==1.6.2 seaborn
```

### 方案B：使用虚拟环境（避免权限问题）

```powershell
# 创建新的虚拟环境
cd c:\Users\admin\Desktop\CLIPasso-main\CLIPasso-main
python -m venv clipasso_venv

# 激活虚拟环境
.\clipasso_venv\Scripts\activate

# 在虚拟环境中安装所有依赖
pip install torch==1.7.1 torchvision==0.8.2
pip install -r requirements.txt
```

### 方案C：最简单 - Google Colab（强烈推荐）

无需任何安装配置，直接使用：
1. 打开 https://colab.research.google.com
2. 上传 `CLIPasso.ipynb`
3. 运行 - 10-15分钟即可完成

## 完整本地安装的后续步骤

如果成功安装了基础依赖，还需要：

1. **安装CLIP (OpenAI)**
   ```bash
   pip install git+https://github.com/openai/CLIP.git
   ```

2. **编译安装diffvg**（需要C++编译环境）
   - 安装 Visual Studio Build Tools
   - 安装 CMake
   - 克隆diffvg仓库并编译

3. **下载U2Net模型**
   ```bash
   gdown https://drive.google.com/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ -O U2Net_/saved_models/
   ```

4. **验证安装**
   ```bash
   python -c "import torch; import pydiffvg; import clip; print('Success!')"
   ```

## 当前状态

- **基础环境**: Python 3.7.0 ✓
- **torch**: 1.7.1 ✓ (CPU版本)
- **torchvision**: 待安装
- **diffvg**: 未安装 ❌
- **CLIP**: 未安装 ❌
- **其他依赖**: 未完成 ❌

## 建议

鉴于Windows环境复杂的权限和兼容性问题，**强烈建议使用Google Colab**来运行这个项目。它可以：
- 避免所有依赖安装问题
- 使用免费的GPU加速
- 在10-15分钟内看到结果