### 1️⃣ Check your current Python version in the venv

```bash
python --version
```

* If it says **3.12.x**, that explains why `TTS` isn’t installing.

---

### 2️⃣ Create a compatible venv (recommended)

Make a new venv with **Python 3.11** (works with latest TTS):

```bash
# Install python 3.11 if not yet installed via Arch
sudo pacman -S python311 python311-venv python311-pip

# Create a new venv using Python 3.11
python3.11 -m venv ~/.global_envs/torch_env_py311

# Activate it
source ~/.global_envs/torch_env_py311/bin/activate

# Upgrade pip
pip install --upgrade pip
```

---

### 3️⃣ Install CPU-only PyTorch + TTS

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install TTS
```

✅ Now it should install correctly.
✅ CPU-only saves disk space.
✅ Compatible Python version.

---

### 4️⃣ Verify installation

```python
python -c "import torch; import TTS; print('Torch:', torch.__version__, 'TTS imported successfully')"
```

---

### 🔹 Notes

* You can still use this environment for your **Vermeil project**.
* If you want GPU later, you can replace the CPU PyTorch wheel with CUDA wheels later.
* Keeping a **shared venv** avoids reinstalling large packages per project.

