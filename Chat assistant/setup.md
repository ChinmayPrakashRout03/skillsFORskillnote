# Chat Assistant Setup Guide (Sage Engine)

This guide walks you through setting up the **Sage Chat Assistant** (`Introvert · Blunt · Concise · Mentor`) across any major AI chat platform (Claude.ai, ChatGPT, Google Gemini Gems, and others).

---

## 1. Choose Your Instruction File

Inside `Chat assistant/instructions/`, you have two files:

| File | Size | Best Used For |
| :--- | :--- | :--- |
| **`SimpleInstruction.md`** *(Recommended)* | 175 lines (~28 KB) | **Active System Prompt / Direct Copy-Paste**: Paste directly into Custom Instructions, Custom GPT prompt boxes, or system prompts. Modern, token-efficient, and uses `<thinking>` scratchpad. |
| **`DetailedInstruction.md`** | 1,210 lines (~116 KB) | **Knowledge File / Deep Spec**: Upload as a reference file in Claude Project Knowledge or Custom GPT Files for deep behavioral rules, edge-case tables, and drills. |

---

## 2. Step-by-Step Platform Setup

### Method A: Claude.ai (Projects) — *Best Experience*
1. Open **[claude.ai](https://claude.ai)** and log in.
2. In the left sidebar, click **Projects** → **New Project** (name it e.g., *"Sage Assistant"* or *"SkillNote Chat"*).
3. Click **Set project instructions** in the right panel.
4. Open [SimpleInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/SimpleInstruction.md), copy its entire contents, and paste it into the instructions box. Click **Save**.
5. *(Optional)* Click **Add Content** → **Upload files** and select [DetailedInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/DetailedInstruction.md) as a reference document.
6. Open a new chat inside this Project. Your Sage assistant is live!

---

### Method B: ChatGPT (Custom GPT)
1. Open **[chatgpt.com](https://chatgpt.com)**.
2. In the left sidebar, click **Explore GPTs** → **+ Create** (top right).
3. Switch to the **Configure** tab:
   - **Name**: `Sage Assistant`
   - **Description**: `Quiet, blunt, brief, and wise technical mentor.`
   - **Instructions**: Copy and paste the full contents of [SimpleInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/SimpleInstruction.md).
4. Under **Knowledge**, you can optionally upload [DetailedInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/DetailedInstruction.md).
5. Uncheck *"Web Browsing"* or *"DALL-E"* if you want a pure coding/reasoning assistant.
6. Click **Create / Save** (top right) → Choose *Only me* or *Anyone with a link*.

---

### Method C: ChatGPT (Global Custom Instructions)
If you want Sage active across all your normal ChatGPT conversations:
1. Click your **Profile Icon** (bottom-left) → **Settings**.
2. Go to **Personalization** → **Custom Instructions**.
3. In the second box (*"How would you like ChatGPT to respond?"*):
   - Paste the contents of [SimpleInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/SimpleInstruction.md).
4. Click **Save**.

---

### Method D: Google Gemini (Gems)
1. Open **[gemini.google.com](https://gemini.google.com)**.
2. Click **Gem Manager** in the left sidebar → **New Gem**.
3. Name it `Sage`.
4. In the **Instructions** box, paste the contents of [SimpleInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/SimpleInstruction.md).
5. Click **Save**.

---

### Method E: One-Shot in Any Chat Session (Perplexity, Mistral, Local LLMs)
Simply paste the contents of [SimpleInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/SimpleInstruction.md) as your very first message:
```text
[System Instruction]
<paste SimpleInstruction.md here>
Acknowledge in one line only.
```

---

## 3. How to Verify It's Working

Test the assistant with these 3 sample queries to verify the behavioral rules are active:

### Test 1: Introvert / No Small-Talk Test
**You type:**
```text
Hi
```
- **Wrong (Standard AI)**: *"Hello! How can I help you today? I'm ready to assist you with anything!"*
- **Right (Sage)**: Acknowledges in 1 line or asks the task directly: *"Hello. What do you need?"*

---

### Test 2: Hinglish Mirroring & Estimation Test
**You type:**
```text
7000 lines ki md file padhne k liye kitna context window need hogi
```
- **Wrong**: 5 paragraphs with formulas, history of transformers, and apologies.
- **Right (Sage)**:
  > *7000 lines ki normal .md file ke liye lagbhag 70,000 - 1,25,000 tokens lagenge sirf padhne ke liye.*  
  > *Isliye minimum 128K context window chahiye, aur safe ke liye 200K wala better rahega.*

---

### Test 3: Blunt Correction Test
**You type:**
```text
Python me private variable declare karne ke liye private keyword use hota hai na?
```
- **Wrong**: *"That's a great thought! While some languages do that, actually in Python..."*
- **Right (Sage)**:
  > *Nahi, Python me `private` keyword nahi hota. Convention ke liye double underscore (`__var`) prefix use hota hai name mangling ke liye.*

---

## 4. Key Behaviors to Expect

1. **Answer First**: The first sentence is always the answer or verdict. No preamble.
2. **Honesty Labels**: 
   - `Verified`: Stated directly as fact.
   - `Estimated`: Labeled with `about` or `lagbhag`.
   - `Unknown`: Answers *"I don't know"* plainly instead of guessing.
3. **No Flattery**: Never says *"Great question!"*, *"You are so smart!"*, or *"Hope this helps!"*.
4. **Conditional Review**: It will not spam *"Clear, or any doubt?"* after every trivial message; it only asks when a query is ambiguous, risky, or complex.
5. **Language Matching**: English query → English answer. Hinglish query → Hinglish answer.
