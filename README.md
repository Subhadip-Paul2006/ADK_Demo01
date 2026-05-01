# 🤖 The Ultimate ADK Agent Master Guide (Python 3.13 Edition)

Yo! Agar tumhare paas ek khali folder hai aur tum ek AI Agent banana chahte ho, toh ye guide tumhare liye hai.  
We fixed the **"Python 3.13 infinite loop"** and the **"Red Text" crashes** so you don't have to. 🚀

---

## 🛠️ Phase 1: The "No-Fail" Installation

Python 3.13 is a beast. Don't use the standard commands. Follow this manual override:

### 1. Create the Environment (Without Pip first!)
```powershell
python -m venv venv --without-pip
```

### 2. Activate the Kitchen
```powershell
.\venv\Scripts\activate
```

### 3. Manually Inject & Upgrade Pip
```powershell
python -m ensurepip --upgrade
python -m pip install --upgrade pip setuptools wheel
```

### 4. Install the Heavyweights (One by one)
```powershell
pip install google-cloud-aiplatform
pip install google-adk
```

---

## 🏗️ Phase 2: Create the Agent Skeleton

Ab framework install ho gaya hai, let's generate the code.

### Run the Creator
```bash
adk create my_agent
```

### The Prompt Choices

- **Choose Model:** Type `1` (Gemini-2.5-Flash)  
- **Choose Backend:** Type `1` (Google AI)  
- **API Key:** Paste your key from AI Studio  
  > ⚠️ Yaad rakhna: Paste karne pe kuch dikhega nahi, just press Enter!

---

## 📝 Phase 3: The "Dumb-Proof" Code Fix

By default, the code might crash because of a missing name. Fix it ASAP.

### Open file:
```
my_agent/agent.py
```

### Replace the `root_agent` part with this:
```python
root_agent = Agent(
    name="my_first_agent",  # <-- CRITICAL: Do not leave this out!
    model="gemini-2.5-flash",
    tools=[get_current_time]
)
```

---

## 🚀 Phase 4: Run & Chat

Waqt aa gaya hai AI se baat karne ka!

### Run Command
```bash
adk run my_agent
```

### Talk to it

Jab `User :` dikhe, type karo:

```
What time is it in Tokyo?
```

---

## ⚠️ Common Error "War Room" (Quick Fixes)

| Error Message           | Reality Check       | Solution                                |
|------------------------|--------------------|------------------------------------------|
| ValidationError: name  | Agent is anonymous | Add `name="something"` in `agent.py`     |
| 401 Unauthorized       | Key issue          | Check `.env` file and restart terminal   |
| (venv) not showing     | Kitchen is closed  | Run `.\venv\Scripts\activate` again      |

---

## 📂 Folder Map

- 📄 `agent.py` → The Brain (Code yahan likho)  
- 🔐 `.env` → The Vault (API Key yahan hai)  
- 📦 `venv/` → The Engine (Isse touch mat karna)  

---

## 🎯 Final Note

Ab jao, world's best AI banao! 🚀  

This covers everything from the `venv` creation to the final chat.  
Copy-paste karke save karo, aur tumhara documentation ekdum professional lagega! 🤘
