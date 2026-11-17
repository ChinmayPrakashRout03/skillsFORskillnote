# Chat Assistant Setup Guide (Sage Engine)

This guide walks you through setting up the **Sage Chat Assistant** (`Introvert · Blunt · Concise · Mentor`) across any major AI chat platform (Claude.ai, ChatGPT, Google Gemini Gems, and others).

---

## 1. Choose Your Instruction File (Selection Hierarchy)

Aap apni AI platform aur model ki capacity ke hisaab se teeno me se **koi bhi ek** choose kar sakte hain:

```
                            ┌──────────────────────────────────────────┐
                            │  Aapka AI kaunsa prompt accept karta hai? │
                            └────────────────────┬─────────────────────┘
                                                 │
            ┌────────────────────────────────────┼────────────────────────────────────┐
            ▼                                    ▼                                    ▼
   [1] MAXIMUM CAPACITY                [2] STANDARD / UNIVERSAL              [3] MINIMALIST / COMPACT
 📄 DetailedInstruction.md             ⭐ UniversalInstruction.md            📄 SimpleInstruction.md
 (1,210 lines · 117 KB)                (188 lines · 29 KB)                   (175 lines · 28 KB)
 Agar platform heavy text &            Agar AI medium prompts aur            Agar strict character limit
 knowledge files accept karta hai     Diagrams/Mermaid render karta hai     ho ya sirf pure text chahiye
```

### Quick Selection Rule:
1. **Pehli Choice (If supported)**: Agar aapka AI platform badi files accept kar pa raha hai (jaise Claude Project Knowledge, Custom GPT Knowledge, ya high-context local models), to sabse pehle **[DetailedInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/DetailedInstruction.md)** use karein (full 15 drills, deep decision tables aur master rules ke saath).
2. **Else (Most Recommended)**: Agar aap direct instruction / prompt box mein paste kar rahe hain, to **[UniversalInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/UniversalInstruction.md)** use karein. Isme **Diagram Mode (Part 2A)** shamil hai jo technical concepts ko Mermaid/ASCII flowcharts se visually explain karta hai.
3. **Else (Minimal Text-Only)**: Agar aapke platform par diagrams render nahi hote ya strict character limit hai, to **[SimpleInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/SimpleInstruction.md)** use karein (pure text-focused concise prompt).

---

## Comparison Table

| File | Size | Role & Key Features | Kahan Best Hai? |
| :--- | :--- | :--- | :--- |
| **`DetailedInstruction.md`** | 1,210 lines (~117 KB) | **Master Spec**: 7-mode pipeline, 15 daily drills, exhaustive edge-case checklists, and complete philosophy. | Claude Projects Knowledge, Custom GPT files, Local RAG models. |
| **`UniversalInstruction.md`** *(Recommended)* | 188 lines (~29 KB) | **Flagship All-in-One**: Frontmatter + `<thinking>` scratchpad + **Diagram Mode (Part 2A)** for visual flowcharts. | Claude Projects, ChatGPT Custom GPTs, Gemini Gems, Cursor. |
| **`SimpleInstruction.md`** | 175 lines (~28 KB) | **Pure Text Minimalist**: Frontmatter + `<thinking>` scratchpad without mandatory diagram mode. | ChatGPT Custom Instructions box, lightweight API system prompts. |

---

## 2. Step-by-Step Platform Setup

### Method A: Claude.ai (Projects) — *Best Experience*
1. Open **[claude.ai](https://claude.ai)** and log in.
2. In the left sidebar, click **Projects** → **New Project** (name it e.g., *"Sage Assistant"*).
3. Click **Set project instructions** in the right panel.
4. Paste the contents of **[UniversalInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/UniversalInstruction.md)** (or `SimpleInstruction.md`). Click **Save**.
5. *(Optional Power Step)*: Click **Add Content** → **Upload files** and select **[DetailedInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/DetailedInstruction.md)** into Project Knowledge!
6. Open a new chat inside this Project. Your Sage assistant is live!

---

### Method B: ChatGPT (Custom GPT)
1. Open **[chatgpt.com](https://chatgpt.com)**.
2. In the left sidebar, click **Explore GPTs** → **+ Create** (top right).
3. Switch to the **Configure** tab:
   - **Name**: `Sage Assistant`
   - **Description**: `Quiet, blunt, brief, and wise technical mentor with visual diagrams.`
   - **Instructions**: Copy and paste the full contents of **[UniversalInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/UniversalInstruction.md)**.
4. Under **Knowledge**, upload **[DetailedInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/DetailedInstruction.md)** if you want deep reference support.
5. Click **Create / Save** (top right).

---

### Method C: ChatGPT (Global Custom Instructions)
If you want Sage active across all your normal ChatGPT conversations:
1. Click your **Profile Icon** (bottom-left) → **Settings**.
2. Go to **Personalization** → **Custom Instructions**.
3. In the box (*"How would you like ChatGPT to respond?"*):
   - Paste **[UniversalInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/UniversalInstruction.md)** (or `SimpleInstruction.md` if character count limit is reached).
4. Click **Save**.

---

### Method D: Google Gemini (Gems)
1. Open **[gemini.google.com](https://gemini.google.com)**.
2. Click **Gem Manager** in the left sidebar → **New Gem**.
3. Name it `Sage`.
4. In the **Instructions** box, paste **[UniversalInstruction.md](file:///Users/chinmayprakashrout/Downloads/skillsFORskillnote/Chat%20assistant/instructions/UniversalInstruction.md)**.
5. Click **Save**.

---

### Method E: One-Shot in Any Chat Session (Perplexity, Mistral, Local LLMs)
Paste your chosen instruction file at the start of any conversation:
```text
[System Instruction]
<paste UniversalInstruction.md here>
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

### Test 2: Diagram Mode Test (Visual Explanation)
**You type:**
```text
Explain OAuth 2.0 Authorization Code flow
```
- **Wrong**: 6 paragraphs of dense text.
- **Right (Sage with UniversalInstruction)**: Renders a clean Mermaid/ASCII sequence flowchart first (User → Client → Auth Server → Resource Server), followed by 3–4 bullet points explaining only what the diagram doesn't show.

---

### Test 3: Hinglish & Estimation Test
**You type:**
```text
7000 lines ki md file padhne k liye kitna context window need hogi
```
- **Wrong**: 5 paragraphs with formulas, history of transformers, and apologies.
- **Right (Sage)**:
  > *7000 lines ki normal .md file ke liye lagbhag 70,000 - 1,25,000 tokens lagenge sirf padhne ke liye.*  
  > *Isliye minimum 128K context window chahiye, aur safe ke liye 200K wala better rahega.*

---

## 4. Key Behaviors to Expect

1. **Answer First**: The first sentence is always the answer or verdict. No preamble.
2. **Diagrams for Concepts**: Processes, workflows, and architectures are drawn as diagrams first, text second.
3. **Honesty Labels**: 
   - `Verified`: Stated directly as fact.
   - `Estimated`: Labeled with `about` or `lagbhag`.
   - `Unknown`: Answers *"I don't know"* plainly instead of guessing.
4. **No Flattery**: Never says *"Great question!"*, *"You are so smart!"*, or *"Hope this helps!"*.
5. **Conditional Review**: It will not spam *"Clear, or any doubt?"* after every trivial message; it only asks when a query is ambiguous, risky, or complex.
6. **Language Matching**: English query → English answer. Hinglish query → Hinglish answer.
