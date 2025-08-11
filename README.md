<div align="center">
  <h1>Vermeil 🧪</h1>
  <p>Your Personal, Low-Cost, and Extensible AI Assistant</p>

  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1000&color=8A2BE2&center=true&vCenter=true&random=false&width=650&lines=A+Customized+AI+Assistant+Powered+by+Phi-3+Mini;Built+for+Efficiency+and+Low-Cost+Operation;Extensible+with+Model+Context+Protocol+(MCP);Coming+Soon%3A+Mobile+%26+IoT+Integration" alt="Typing SVG" />

</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge" alt="Project Status">
  <a href="https://github.com/Matrixxboy/vermeil/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  </a>
  <a href="https://github.com/Matrixxboy/vermeil/stargazers">
    <img src="https://img.shields.io/github/stars/Matrixxboy/vermeil?style=for-the-badge&logo=github&color=gold" alt="GitHub Stars">
  </a>
</p>

## 🚀 About Vermeil

Vermeil is a lightweight, powerful, and cost-effective AI assistant designed to run efficiently on your local machine. At its core is **Vermeil**, a customized Large Language Model (LLM) based on Microsoft's `phi3:mini`, fine-tuned for high-quality, responsive interaction.

The project's main goal is to make advanced, personalized AI accessible to everyone without the high costs of proprietary cloud services. With a focus on modularity, Vermeil can be extended using the **Model Context Protocol (MCP)**, allowing you to integrate your own data and tools seamlessly.

## ✨ Key Features

- **🧠 Custom LLM:** Powered by a fine-tuned `phi3:mini` model for optimal performance and quality.
- **💸 Low-Cost:** Engineered to minimize resource consumption, making it perfect for local deployment.
- **🔧 Extensible Architecture:** Easily add new capabilities and context using the **Model Context Protocol (MCP)**.
- **🐍 Python-Powered:** Built with Python 3.10 for modern, robust performance.
- **🔜 Cross-Platform Vision:** Currently available for desktop, with mobile and IoT versions on the horizon!

## 🚧 Project Status: Under Active Development

**Vermeil is currently under heavy development.** Features are being added and improved continuously. While the core functionality is operational, you may encounter bugs. We appreciate your patience and welcome contributions to help us build a stable and feature-rich application.

## 🛠️ Getting Started

Follow these steps to get Vermeil running on your local machine.

### Prerequisites

-   **Ollama:** Vermeil uses Ollama to run the local LLM.
-   **Python 3.10:** This project is built and tested with Python 3.10. It is **highly recommended**.
-   **Git:** To clone the repository.

### Step 1: Install and Set Up Ollama

1.  **Install Ollama:**
    -   **For macOS & Linux:**
        ```sh
        curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
        ```
    -   **For Windows:**
        Download and run the installer from the [**Ollama website**](https://ollama.com/download).

2.  **Download the Base Model:**
    After installing Ollama, open your terminal and pull the `phi3:mini` model. This is the foundation for Vermeil.
    ```sh
    ollama pull phi3:mini
    ```

3.  **Create the Custom 'vermeil' Model:**
    Vermeil is designed to work with a custom model entry. In the root of this project, you will find a `Modelfile`. Use it to create the `vermeil` model by running:
    ```sh
    ollama create vermeil -f Modelfile
    ```
    You can verify the model was created by running `ollama list`.

### Step 2: Configure and Install the Project

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Matrixxboy/vermeil.git](https://github.com/Matrixxboy/vermeil.git)
    cd vermeil
    ```

2.  **Set Model Configuration:**
    Open the configuration file located at `core_project/core/Model/model_config.py`.
    Ensure the following variables are set to point to your local Ollama instance and the custom model:
    ```python
    OLLAMA_URL = "http://localhost:11434/api/generate"
    OLLAMA_MODEL = "vermeil"
    ```

3.  **Create a Virtual Environment & Install Dependencies:**
    ```sh
    python3.10 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

### Step 3: Run the Application

Once Ollama is running and the project is configured, launch the application:
```sh
python main.py
```

## 🧩 Extending with Model Context Protocol (MCP)

One of **Vermeil's** most powerful features is its **extensibility**.  
MCP allows you to inject **custom context, tools, or data** into the model before it processes a prompt.  
This enables you to tailor Vermeil's knowledge and capabilities to your specific needs.

### 🔧 How to add your own context
1. Navigate to the `core_project/MCP/` directory.
2. Add your **custom protocol files** or modules in this directory.
3. The application will automatically detect and load them, making them available to the LLM.

> This system is designed to be simple yet powerful, allowing for deep customization without altering the core codebase.

---

## 🗺️ Roadmap
We have an exciting future planned for Vermeil! Here's what we're working on:

- [x] Core AI Assistant (Desktop)  
- [ ] Fully-featured Mobile Application  
- [ ] IoT Device Integration for smart home commands  
- [ ] Advanced Tool Integration via MCP  
- [ ] Community-driven MCP library  
- [ ] Further performance and cost-optimization research  

---

## 🤝 Contributing

Contributions are what make the **open-source community** such an amazing place to learn, inspire, and create.  
Any contributions you make are greatly appreciated.  

If you have a suggestion that would make this better:  
- Fork the Project  
- Create your Feature Branch  
  ```bash
  git checkout -b feature/AmazingFeature
  ```

- Commit your Changes
  ```bash
  git commit -m 'Add some AmazingFeature'
  ```

- Push to the Branch
  ```bash
  git push origin feature/AmazingFeature
  ```

Open a Pull Request



---

## 📄 License

Distributed under the **MIT** License.
See LICENSE for more information.

<p align="center">Stay tuned for more updates! 🚀</p>

