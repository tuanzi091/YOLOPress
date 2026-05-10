@echo off
echo =========================================
echo CLIPasso 安装脚本 - Windows版本
echo =========================================
echo.

cd /d "%~dp0"

echo [步骤1] 创建虚拟环境...
if exist clipasso_venv rmdir /s /q clipasso_venv
python -m venv clipasso_venv
call clipasso_venv\Scripts\activate.bat

echo.
echo [步骤2] 升级pip...
python -m pip install --upgrade pip

echo.
echo [步骤3] 安装PyTorch...
pip install torch==1.7.1 torchvision==0.8.2 -i https://pypi.tuna.tsinghua.edu.cn/simple

echo.
echo [步骤4] 安装CLIP...
pip install git+https://github.com/openai/CLIP.git

echo.
echo [步骤5] 安装基础依赖...
pip install numpy pillow matplotlib tqdm pandas
pip install scikit-image scipy seaborn scikit-learn
pip install svgwrite svgpathtools cssutils numba

echo.
echo [步骤6] 安装其他工具依赖...
pip install imageio opencv-python wandb visdom
pip install ftfy regex gdown torch-tools

echo.
echo =========================================
echo 基础安装完成！
echo =========================================
echo.
echo 重要：接下来需要安装diffvg
echo 1. 安装Visual Studio Build Tools (如果还没有)
echo 2. 运行: git clone https://github.com/BachiLi/diffvg.git
echo 3. cd diffvg
echo 4. git submodule update --init --recursive
echo 5. python setup.py install
echo.
echo 或者下载预编译的diffvg wheel文件。
echo.
echo 然后下载U2Net模型:
echo gdown https://drive.google.com/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ -O U2Net_/saved_models/
echo.
echo 运行项目:
echo python run_object_sketching.py --target_file "camel.png"
echo.
pause