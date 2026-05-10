# CLIPasso 快速安装指南

## 在 Windows 上成功运行 CLIPasso 的步骤

### 准备工作

1. **打开PowerShell或命令提示符（管理员）**
   - 右键点击"开始"菜单
   - 选择"Windows PowerShell (管理员)"或"终端 (管理员)"

2. **导航到项目目录**
   ```powershell
   cd "C:\Users\admin\Desktop\CLIPasso-main\CLIPasso-main"
   ```

### 步骤1：创建虚拟环境

```powershell
# 删除旧的虚拟环境（如果存在）
if (Test-Path clipasso_venv) { Remove-Item -Recurse -Force clipasso_venv }

# 创建新的虚拟环境
python -m venv clipasso_venv

# 激活虚拟环境
.\clipasso_venv\Scripts\activate
```

### 步骤2：升级pip

```powershell
python -m pip install --upgrade pip
```

### 步骤3：安装PyTorch

```powershell
# 安装CPU版本的PyTorch（避免CUDA兼容问题）
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

或者使用清华镜像：

```powershell
pip install torch==1.7.1 torchvision==0.8.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 步骤4：安装CLIP (OpenAI)

```powershell
pip install git+https://github.com/openai/CLIP.git
```

### 步骤5：安装diffvg（最关键但最复杂）

diffvg是此项目的核心依赖，需要C++编译环境。

**5.1 首先安装编译工具**

如果你没有Visual Studio Build Tools，需要安装：

1. 下载 Visual Studio Build Tools 2022：
   https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022

2. 安装时选择"使用C++的桌面开发"

**5.2 安装CMake**

```powershell
pip install cmake
```

**5.3 克隆并编译diffvg**

```powershell
# 克隆diffvg仓库
git clone https://github.com/BachiLi/diffvg.git
cd diffvg

# 初始化子模块
git submodule update --init --recursive

# 编译安装
python setup.py install
cd ..
```

### 步骤6：安装其他Python依赖

```powershell
pip install numpy pillow matplotlib tqdm pandas
pip install scikit-image scipy seaborn scikit-learn
pip install svgwrite svgpathtools cssutils numba
pip install imageio opencv-python wandb visdom
pip install ftfy regex gdown torch-tools
```

### 步骤7：下载U2Net预训练模型

```powershell
# 模型会自动下载，如果失败，手动下载：
gdown https://drive.google.com/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ -O U2Net_/saved_models/
```

### 步骤8：验证安装

```powershell
python -c "import torch; import pydiffvg; import clip; print('All imports successful!'); print('PyTorch version:', torch.__version__)"
```

### 步骤9：运行项目

```powershell
# 使用示例图片运行
python run_object_sketching.py --target_file "camel.png"

# 或使用Jupyter Notebook
jupyter notebook CLIPasso.ipynb
```

## 推荐的运行参数

对于快速测试：
```powershell
python run_object_sketching.py --target_file "camel.png" --num_strokes 16 --num_sketches 1 -cpu
```

对于更好效果：
```powershell
python run_object_sketching.py --target_file "camel.png" --num_strokes 32 --num_sketches 3
```

## 输出位置

生成的SVG草图文件保存在：
`output_sketches/<图片名>/`

## 常见问题

### 问题1：diffvg编译失败
**解决方案**：确保已安装Visual Studio Build Tools和CMake

### 问题2：torchvision安装失败
**解决方案**：分开安装，先装torch再装torchvision

### 问题3：CUDA版本不匹配
**解决方案**：使用CPU版本的PyTorch（较慢但兼容性更好）

## 重要提示

⚠️ **diffvg安装最复杂** - 这是项目能否运行的关键

⚠️ **完整安装需要时间** - 依赖包下载和编译可能需要1-2小时

⚠️ **建议使用Google Colab** - 如果遇到困难，这是最快的方法

## 项目文档

已创建以下文档供参考：
- `COLAB_RUN_GUIDE.md` - Google Colab快速开始
- `WINDOWS_INSTALLATION_GUIDE.md` - 详细Windows安装说明
- `LOCAL_INSTALLATION_SUMMARY.md` - 本地安装问题总结
- `QUICK_START_GUIDE.md` - 本快速开始指南

## 如果你想快速体验

打开浏览器访问：https://colab.research.google.com

上传`CLIPasso.ipynb`文件，点击运行，10-15分钟即可看到结果！