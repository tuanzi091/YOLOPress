# CLIPasso 在 Windows 上的安装说明

## 环境要求
- Python 3.7+
- NVIDIA GPU (用于加速，推荐)
- CUDA 10.1+ (如果使用GPU)

## 安装步骤

### 1. 创建虚拟环境
```bash
cd c:\Users\admin\Desktop\CLIPasso-main\CLIPasso-main
python -m venv clipasso_env
.\clipasso_env\Scripts\activate
```

### 2. 安装 PyTorch
由于这个项目需要特定版本的PyTorch (1.7.1)，并且你的系统CUDA版本较新(13.2)，建议：

**选项A：使用PyTorch 1.7.1 (CUDA 10.1)**
```bash
pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

**选项B：使用较新版本PyTorch (可能部分功能不兼容)**
```bash
pip install torch>=1.8.0 torchvision
```

### 3. 安装 CLIP (OpenAI)
```bash
pip install git+https://github.com/openai/CLIP.git
```

### 4. 安装 diffvg (关键依赖)
diffvg是这个项目最重要的依赖，用于可微分的矢量图形渲染。在Windows上安装比较复杂：

```bash
# 首先安装cmake和其他构建工具
pip install cmake

# 克隆diffvg仓库
git clone https://github.com/BachiLi/diffvg
cd diffvg
git submodule update --init --recursive

# 安装diffvg (可能需要Visual Studio构建工具)
python setup.py install
```

### 5. 安装其他依赖
```bash
pip install numpy pillow matplotlib tqdm pandas scikit-image
pip install svgwrite svgpathtools cssutils numba
pip install imageio opencv-python scikit-learn scipy seaborn
pip install wandb visdom
pip install ftfy regex gdown
pip install torch-tools
```

### 6. 下载 U2Net 预训练模型
```bash
# 模型会自动下载，但如果需要手动下载：
gdown https://drive.google.com/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ -O U2Net_/saved_models/
```

### 7. 验证安装
```bash
python -c "import torch; import pydiffvg; import clip; print('All imports successful!')"
```

## 常见问题

### 问题1：PyTorch下载超时
**解决方案**：使用国内镜像源
```bash
pip install torch==1.7.1 torchvision==0.8.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题2：diffvg编译失败
**解决方案**：diffvg需要完整的C++编译环境
- 安装 [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/)
- 确保选择 "C++ build tools" 选项
- 设置环境变量：`set CL.exe=C:\Program Files (x86)\Microsoft Visual Studio\...\VC\Tools\MSVC\...\bin\Hostx64\x64\cl.exe`

### 问题3：CUDA版本不匹配
**解决方案**：
- 检查GPU兼容的CUDA版本：`nvidia-smi`
- 如果CUDA太新，使用CPU版本：`pip install torch==1.7.1+cpu torchvision==0.8.2+cpu -f https://download.pytorch.org/whl/torch_stable.html`

## 运行项目

### 方法1：使用提供的脚本
```bash
cd c:\Users\admin\Desktop\CLIPasso-main\CLIPasso-main
python run_object_sketching.py --target_file "camel.png"
```

### 方法2：使用Jupyter Notebook
```bash
jupyter notebook CLIPasso.ipynb
```

## 推荐的参数设置

对于RTX 4080等现代GPU：
```bash
python run_object_sketching.py --target_file "camel.png" --num_strokes 16 --num_sketches 1 -cpu
```

如果GPU可用：
```bash
python run_object_sketching.py --target_file "camel.png" --num_strokes 32 --num_sketches 3
```

## 注意事项

1. **GPU内存**：RTX 4080有16GB显存，应该足够运行
2. **运行时间**：每个sketch可能需要5-15分钟
3. **输出位置**：生成的SVG文件保存在 `output_sketches/` 目录