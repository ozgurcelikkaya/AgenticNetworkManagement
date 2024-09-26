# Agentic-Network-System
## Steps to set up the environment and run the system:
1. Open your terminal and run the following command to install all necessary packages:

```
pip install -r requirements.txt
```

2. In the terminal, run the **network_groupchat.py** script:

```
python network_groupchat.py
```

3. Next, run the all tools scripts:

```
python check_interface_status.py

```

4. Finally, execute the **chat_inference.py** script:

```
python chat_inference.py
```

# LiteLLM Proxy Server

## Steps to set up the environment and run the system:

1. Open your terminal and run the following command to install all necessary packages:

```
pip install -r requirements.txt
```

2. Execute the following command to pull the gemma2:2b model from Ollama:
   
```
ollama pull gemma2:2b
```

4. After pulling the model, start the LiteLLM server with the specified model:

```
litellm --model ollama/gemma2:2b
```

4. Finally, execute the main script to start the multi-agent system:
   
```
python agentic_system.py
```
