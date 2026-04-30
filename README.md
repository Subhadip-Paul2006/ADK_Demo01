# 🤖 My First AI Agent (ADK Skeleton) 

Yo! Agar tum yahan tak pahunch gaye ho, toh congrats! 🥳 Tumne Python 3.13 ke dangerous loop ko hara diya hai. This folder is the **Brain** of your AI. Isko set karne ke liye niche ke steps follow koro, ekdom easy logic!

---

### 🛠️ Step-by-Step: Zero to Hero (Terminal Setup)

Follow these steps exactly, aur tumhara agent makhon er moto (like butter) cholbe.

1.  **Activate the Kitchen (Venv):**
    Sabse pehle apna environment chalu karo. Environment active na thakle kichu kaj korbe na!
    ```powershell
    .\venv\Scripts\activate
    ```
    *(Terminal prompt ke aage `(venv)` dikhna chahiye. Setai tomar green signal!)*

2.  **The "Run" Command:**
    Apne agent ko zinda karne ke liye ye type karo:
    ```bash
    adk run my_agent
    ```

3.  **Chat with the Beast:**
    Jab `User :` likha aaye, tab usse sawal pucho!
    *   **Try this:** `What time is it in Tokyo?`
    *   **Logic:** Ye dummy agent humare `get_current_time` function ko use karke answer dega.

---

### ⚠️ Error "War Room": Red Text Se Kaise Lade? 🧨

Agar terminal pe khoon (Red Error) dikhe, toh ghabrana mat. Just check these 3 things:

#### 1. The "Anonymous Agent" Crash
*   **Error:** `ValidationError: 1 validation error for LlmAgent... name field required`.
*   **Solution:** Open `agent.py`. Make sure `Agent(` has a `name="something"` line inside it. Google ADK anonymous agents ke allow kore na!

#### 2. The "Invisible Key" Problem
*   **Error:** `401 Unauthorized` or a long Traceback.
*   **Solution:** Go to your `.env` file. Check if your `GOOGLE_API_KEY` is there. 
*   **Pro Tip:** Agar `.env` update kiya hai, toh terminal ko **Close** karke **New Terminal** open karo, tabhi changes apply honge!

#### 3. The "Python 3.13" Loop
*   **Problem:** Installation stuck at "Searching for versions..."
*   **Solution:** Refer to the **ADK_Setup_Guide.md**. Use the 3-step manual install instead of the single command!

---

### 📂 Folder Structure (Ki Ache Ei Folder e?)

*   📄 **`agent.py`**: The heart. Yahan tum AI ko commands dete ho aur Tools (functions) add karte ho.
*   🔐 **`.env`**: Your secret vault. Isme API key rehti hai. Isse kabhi kisi ko share mat karna (Don't push to GitHub!).
*   📦 **`__init__.py`**: Python ko batata hai ki ye ek valid project folder hai. Touch mat karna!

---

### 🔥 Final Pro Tip
Agent ko band karne ke liye terminal pe `exit` likho ya `Ctrl + C` press karo. 

**Ab jao, world's best AI banao! 🚀**
