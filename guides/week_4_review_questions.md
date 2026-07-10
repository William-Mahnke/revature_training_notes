# Week 4 - Review Questions

The following are specific questions related to concepts covered in Week 4 of training. If you are able to confidently answer the questions in this review guide, you should be able to confidently answer any question related to the week 4 material.

## AI, Machine Learning, and Generative AI Foundations

**What is the difference between AI, Machine Learning, and Generative AI, and how do these three terms relate to one another?**

- AI is the broadest term — any technique that gets a computer to do something we'd normally consider to require human intelligence. Machine learning is a subset of AI where the system learns patterns from data instead of following hand-written rules. Generative AI is a newer branch of ML that produces new content (text, code, images) rather than just classifying or predicting on existing input. They nest inside each other: ML is a kind of AI, and generative AI is a kind of ML.

**Why does not all AI involve "learning"? Give an example of a rules-based AI system.**

- Not all AI learns from data. Many systems are just large sets of human-written rules the computer follows. A data pipeline rule like "if a record is missing a customer_id, send it to the error table; otherwise load it to the warehouse" is rules-based AI — a human anticipated every case and wrote the logic in advance.

**What is a rules-based system good at, and what is its fundamental limitation?**

- Rules-based systems are predictable, easy to explain, and auditable — great for deterministic work like validation and routing. Their limitation is that a human has to anticipate every situation in advance; the moment reality presents a case nobody wrote a rule for, the system has no idea what to do.

**What is Machine Learning, and how does it differ from traditional rule-based programming?**

- Machine learning is an approach where you show the system many examples and let it work out the patterns on its own, rather than a human writing the rules. In traditional programming, rules plus input produce output; in ML, examples produce the model (the rules), and the model makes predictions on new input.

**In machine learning, what does the human provide instead of writing the rules?**

- The human provides training examples — data that shows the system what the patterns look like. In supervised learning, those examples also include the correct answers (labels).

**What is training, and what are the parameters that result from it?**

- Training is the process of showing a model many examples so it can extract patterns. Those patterns are stored as internal numbers called parameters (also called weights). Once trained, the model uses those parameters to make predictions on new data.

**What does generalization mean?**

- Generalization is a model's ability to handle new, unseen input — not just the examples it was trained on. A model that only works on its training data is useless; the whole point of ML is to apply learned patterns to data it has never seen before.

**What is the difference between supervised and unsupervised learning?**

- In supervised learning, training examples come with the right answers attached (labels) — like transactions labeled "fraud" or "legitimate." In unsupervised learning, the data has no labels, and the model groups or organizes it on its own, such as discovering natural clusters in customer segments.

**What does it mean for training data to be "labeled," and which type of learning relies on it?**

- Labeled data means each training example has the correct answer attached — a transaction marked as fraud, a review tagged as positive. Supervised learning relies on labeled data; unsupervised learning does not.

**What is the difference between the training phase and the prediction phase of a model?**

- During training, the model learns patterns from many labeled (or unlabeled) examples and stores them in its parameters. During prediction, the trained model takes new input it has never seen and produces an output — a label, a score, or a forecast — using only what it learned.

**Why is writing hand-coded rules a poor approach for a problem like fraud detection?**

- Fraud shows up in countless combinations across amounts, timing, location, merchant patterns, and device signals, and the patterns shift as fraudsters adapt. No human can write rules for every combination. ML handles this by learning from millions of past transactions labeled fraud or legitimate, finding patterns you'd never anticipate by hand.

**What is Generative AI, and how does it differ from models built to classify or predict?**

- Generative AI produces brand new content — text, code, images, audio — rather than outputting a label or number about existing input. Traditional ML models answer questions like "is this fraudulent?" or "will this customer churn?"; generative models create something that didn't exist before.

**What does it mean for a model to be "generative"?**

- A generative model creates new content from a prompt by repeatedly predicting what comes next based on statistical patterns learned from training data. It doesn't retrieve existing answers — it generates plausible new output token by token.

**Name three types of content that Generative AI can produce.**

- Text, code, and images (audio is also a common output).

**At its heart, how does a generative model produce new content?**

- It's prediction at enormous scale. A text-generating model has learned statistically what tends to come next given what came before. It repeatedly predicts the next most likely chunk of text, appends it, and loops until a full response is produced.

**What does it mean that a generative model is optimized to be "plausible" rather than "true"?**

- The model is trained to produce output that looks like a correct answer, not output that is verified to be correct. Most of the time plausible and true align, but when they don't, the model will hand you a confident, well-formatted, completely wrong answer with no signal that something is off.

**How are rules-based AI, machine learning, and generative AI each used in a modern data stack? Give an example of each.**

- Rules-based AI handles deterministic work — data validation rules, scheduling, routing malformed records to error tables. Machine learning powers predictive features — fraud scoring, anomaly detection, entity resolution, demand forecasting. Generative AI powers newer features — generating SQL from plain language, drafting dataset documentation, summarizing data quality results, and coding assistants.

## Large Language Models

**What is a Large Language Model?**

- A large language model (LLM) is a generative model trained on an enormous body of text — books, articles, documentation, and source code — to predict the next unit of text given everything that came before.

**What single task is an LLM fundamentally trained to do?**

- Predict the next token given all preceding tokens. A full response is just that prediction loop running hundreds of times.

**What is a token, and roughly how much text does one represent?**

- A token is roughly a word or a piece of a word. "Pipeline" might be one token; "unpartitioned" might break into "un," "partition," and "ed."

**Describe the loop an LLM follows to generate a full response.**

- The model reads your input as a sequence of tokens, predicts the most likely next token, appends it to the sequence, and repeats. Each step considers everything generated so far and asks "what is the most likely next token?" until the response is complete.

**What is the word "large" actually referring to in "Large Language Model"?**

- The scale — billions of internal parameters trained on trillions of tokens. That scale is what allows fluent, context-aware text rather than gibberish.

**What is a parameter in the context of an LLM, and why does scale matter?**

- A parameter is one of the internal numbers (weights) the model learned during training that encode patterns in language. More parameters and more training data generally mean better fluency and broader knowledge, though the model is still predicting likely text, not retrieving verified facts.

**Why does an LLM's training data cutoff matter in daily use?**

- The model knows nothing about events, library versions, or APIs that appeared after training ended. It will still answer confidently about them, often by inventing something plausible rather than admitting the gap.

**What is a context window?**

- The finite amount of text a model can consider at once — your instructions, conversation history, and any code you paste all have to fit inside it. When a conversation gets long, the earliest details can effectively fall out of view.

**At a high level, what distinguishes GPT, Claude, Gemini, Llama, and BERT from one another?**

- GPT (OpenAI), Claude (Anthropic), and Gemini (Google) are closed, API-accessed generative models with strong general-purpose performance. Llama (Meta) is open-weight — downloadable and runnable on your own infrastructure. BERT (Google) is older and built for understanding and classifying text rather than generating it.

**What is the difference between a generative model and an "understanding" model like BERT? Give an example task for each.**

- Generative models (GPT, Claude, Gemini, Llama) continue a sequence — drafting a dataset summary or writing a function. Understanding models like BERT analyze a complete piece of text and produce a classification or representation — tagging support tickets by topic or scoring product review sentiment.

**What is the difference between a closed model and an open-weight model, and why is it a data-control decision rather than a quality judgment?**

- A closed model lives on the vendor's servers; you send text and get a response back. An open-weight model like Llama can run entirely in your own environment. This isn't about which is "better" — it's about whether you can send sensitive data to a third party or need to keep it in-house.

**Name four realistic use cases for an LLM, and state the boundary or risk attached to each.**

- Drafting and rewriting text — works well, but you must check facts because it states false things fluently. Summarizing long content — condenses well, but can drop or invent key details. Explaining code or errors — strong on patterns, but may explain code that does something subtly different. Generating code and tests — highly patterned, but hallucinates methods and APIs you must read, run, and test.

**What kinds of tasks do LLMs excel at, and what kinds do they struggle with?**

- They excel at language-shaped work — drafting, summarizing, explaining, generating code, classifying text — especially where you can verify the output. They struggle where ground truth is required and they don't have it: current events past their training cutoff, your specific system state, proprietary schemas, and tasks requiring verified factual accuracy without a source to check against.

**What does it mean that "you remain the source of truth" when using an LLM?**

- The model produces a strong first draft, but you are responsible for verifying correctness. It has no stake in whether the output is accurate — that judgment is always yours.

## Prompt Engineering

**What is prompt engineering, and why does it actually work given how an LLM generates text?**

- Prompt engineering is structuring your input to get reliable, useful output. It works because the model generates the most likely continuation of whatever you give it — a clearer, more constrained input narrows the space of likely continuations toward what you actually want.

**Why can the same model produce very different outputs depending on how it is prompted?**

- The model continues from whatever context you provide. Different wording, examples, constraints, or roles shift the statistical space of likely next tokens, producing very different outputs from the same underlying model.

**Name some characteristics of an effective prompt.**

- Give context, not just a request. State constraints up front. Set a role or audience. Include worked examples when format matters. Be specific about language, libraries, return types, and edge cases.

**What is zero-shot prompting, and when is it the right default?**

- Zero-shot means asking the model to do something without giving examples of a good answer — you just describe the task. It's the right default for well-known tasks the model has seen extensively in training, like sentiment classification or summarization.

**What is few-shot prompting, and what problem does it solve?**

- Few-shot prompting includes a small number of worked examples before the real request. It solves inconsistent output or format problems by showing the model exactly the pattern you expect.

**How do worked examples in a few-shot prompt "condition" the model?**

- The examples demonstrate the exact format and reasoning pattern you want. The model continues that demonstrated pattern when completing the real request, because statistically the most likely continuation matches the template you showed.

**What is the trade-off of adding more examples to a few-shot prompt?**

- More examples improve consistency and format lock-in, but each example consumes space in the context window. Use as few as get the job done.

**What is conditioning, and what are three ways to condition a model besides giving examples?**

- Conditioning is shaping the model's behavior through input rather than changing the model itself. Three ways besides examples: explicit instructions, constraints (e.g., "use only the standard library"), and setting a role or audience (e.g., "explain for a non-technical stakeholder").

**Why does giving context rather than just a request produce better output? Give an example.**

- Specific context narrows the space of likely continuations. "Write a function to load some data" produces generic output; "Write a Python function `load_to_warehouse` that takes a pandas DataFrame and a table name, writes it to Postgres using SQLAlchemy, and returns the number of rows written" produces something you can almost use directly.

**Why is it useful to state constraints up front in a prompt?**

- Constraints prevent the model from reaching for things you don't have or don't want. Saying "use only the standard library, no external dependencies" stops it from importing packages that aren't in your environment.

**How does setting a role or audience change a model's output?**

- The model adjusts tone, depth, and vocabulary to match the framing. "Explain this for a non-technical stakeholder in two sentences" produces a very different answer than the same question with no audience specified.

**Are LLM conversations stateful or stateless? Explain the behavior within a session versus across sessions.**

- Stateful within a session, stateless across sessions. Within one conversation, the entire history is fed back into the model on every turn, so it appears to remember prior messages. Across sessions, nothing carries over — each new conversation starts fresh.

**How does a model appear to "remember" earlier parts of a conversation?**

- The whole conversation so far is included in the input on every turn. The model doesn't have persistent memory — it re-reads the full history each time and continues coherently from it.

**Why is it better to iterate on a close-but-wrong answer than to restart the conversation?**

- When you say specifically what to fix, the model has the prior context and refines rather than starting over. Restarting throws away useful context and often produces a different wrong answer instead of a correction.

**Why can a very long conversation start to drift, and what is often the fix?**

- Because the entire history is reconsidered each turn, a long or muddled conversation can pull the model in a bad direction. Starting a fresh conversation often produces a cleaner result than fighting accumulated context.

**Why must you mind the context window during a long session, and what should you do if something important was established far back?**

- Everything must fit in the finite context window, and earliest details can fall out of view. If something important was established early, restate it explicitly rather than assuming the model still has it.

**What is fine-tuning, and how does it differ from prompting?**

- Fine-tuning continues training an existing model on a focused, specialized dataset, actually changing its internal parameters. Prompting changes behavior through input only — the model itself is unchanged.

**When is fine-tuning the appropriate tool rather than prompting?**

- When you have a narrow, repeated, high-volume problem that prompting has proven insufficient for — a recurring task where you need the model to internalize domain-specific patterns rather than be steered each time.

**Summarize the trade-offs between prompting/conditioning and fine-tuning.**

- Prompting is instant, free, reversible per request, and should be your first resort. Fine-tuning requires a dataset, compute, time, and cost, produces a new specialized model, and is reserved for when the lighter approach has been exhausted.

## AI Coding Tools and Autonomy Levels

**What is a hallucination, and what root cause produces it?**

- A hallucination is confident, plausible output that isn't correct — a method that doesn't exist, a package that was never published, a fact that isn't true. The root cause is that the model is optimized to produce statistically likely text, not verified truth.

**Why is a confident, well-formatted answer not evidence that it is correct?**

- The model has no mechanism to verify its output. Fluency and formatting are products of its training on well-written text, not indicators of accuracy. It will present wrong answers with the same confidence as right ones.

**Why is verifying against authoritative sources the standard control for hallucination?**

- Since the model can't self-verify, the only reliable check is comparing its output against something authoritative — official documentation, your actual schema, a real system state, or code you run and test.

**Why is framing AI coding work as "pair programming" useful, and which role are you always in?**

- It keeps you engaged rather than passively accepting output. The model is a fast, knowledgeable, occasionally overconfident driver; you are always the navigator — setting direction, deciding what's worth keeping, and catching mistakes.

**How is using an AI coding tool different from using a search engine?**

- A search engine returns existing answers you look up and leave. An AI coding tool works alongside you in real time on the same problem — generating, explaining, and iterating on code as a partner, not a lookup.

**What is the "autonomy" dial, and why does the risk change as autonomy increases?**

- Autonomy is how much the tool acts on your behalf versus waits for you to act. As autonomy increases, so does both potential impact and potential for unintended consequences — more files touched, more commands run, larger blast radius before you see anything.

**Describe Level 1 (autocomplete) AI assistance.**

- The model watches what you type and predicts what comes next inline in the editor. You accept with Tab. Nothing happens until you decide. It works one suggestion at a time with no file access beyond the current file and nearby context.

**Describe Level 2 (conversational) AI assistance.**

- You describe what you want in a chat window and the model returns code or an explanation. You copy and apply it yourself — the tool does not act on your project. Even if it can see your files, you remain the bridge between its suggestion and your codebase.

**Describe Level 3 (in-editor chat with gated approval) and what defines this level.**

- The tool reads your project and acts on it directly through tools — writing files, running commands, calling APIs — in an observe-decide-act loop. At gated Level 3, it pauses for your approval before each write or command. This is the default for most modern agent tools.

**What two properties make a system "agentic"?**

- Tool use — it can read/write files, run commands, call APIs. And an iterative loop — it chooses what to do next based on what it just observed, rather than producing one answer and stopping.

**What is the difference in blast radius between a gated (Level 3) and an autonomous (Level 4) tool?**

- Gated Level 3 pauses before each action, so you approve changes as they happen and the blast radius stays small. Ungated Level 4 (autonomous) executes writes and commands without pausing — it can modify many files and run commands with real side effects before you see anything.

**Why should you commit to git before running an agentic tool on a real project?**

- An ungated agent can modify code across many files before you review the outcome. Committing first gives you a clean revert point if the agent's work goes wrong.

**Why are passing tests not a substitute for reading an agent's diff?**

- The agent may have taken a path you wouldn't have chosen, introduced technical debt, or written tests that pass without asserting the right behavior. Tests generated by the same model that wrote the code are especially unreliable as a safety net.

**What is GitHub Copilot?**

- GitHub's AI coding assistant integrated into editors like VS Code and JetBrains. It covers autocomplete, chat, and agentic modes, and is the most widely deployed assistant in industry.

**How do Copilot's autocomplete, chat, and agent modes map onto the levels of autonomy?**

- Autocomplete is Level 1. Chat is Level 2 — it returns suggestions you apply yourself. Agent mode is Level 3 — it reads your project and acts on it through tools, gated by default.

**What controls whether a Copilot agent operates at Level 3 versus Level 4?**

- Configuration, not the prompt. Gated Level 3 pauses for approval before each write or command (the default). Removing that gate — for example via autopilot or `--allow-all` flags — makes it ungated Level 4, where you review outcomes rather than each step.

**What should you watch for in Copilot's autocomplete suggestions, and why?**

- Hallucinated method names, outdated API usage, missing imports, and wrong assumptions about your schema. Autocomplete looks plausible inline but may reference libraries or APIs that don't exist in your version or environment.

**What transfers between AI coding tools, and what merely changes?**

- The rhythm transfers completely — accepting suggestions, giving real project context, reviewing diffs before accepting. Only the keybindings and billing change between tools.

## Developing with GenAI

**What does it mean to give context rather than just a request when prompting for code? Give a before/after example.**

- It means naming the language, library, return type, and edge cases so the model narrows its output. Before: "Write a function to get a record by ID." After: "Write a Python function `get_order_by_id` using SQLAlchemy. Return the Order row or None if not found. The orders table has an integer id column."

**Why would you ask a model to explain code before it modifies it?**

- It catches misunderstandings early, before they become wrong code. When inheriting unfamiliar code, understanding what it actually does prevents the model from "fixing" something that wasn't broken or missing fragile logic.

**Why request tests alongside the implementation rather than afterwards?**

- It forces the model to reason about edge cases while writing the code. You're more likely to get implementation that handles null inputs, empty data, and error paths when tests are part of the same request.

**Why is AI particularly strong at writing tests, and what should you watch for?**

- Tests are structured, follow predictable patterns, and don't require deep business logic understanding. Watch for tests that pass but don't assert the right thing, and missing edge cases specific to your domain.

**What makes good AI-generated documentation, and what is the failure mode to avoid?**

- Good documentation explains intent and behavior for a specific audience — what the function is for, what happens in edge cases. The failure mode is generic comments that describe syntax rather than intent, like "this method returns a user."

**How is AI useful for code analysis, and what are its limits?**

- It's a fast second set of eyes for gut-checks — reviewing for unhandled None values, fragile logic, or edge cases before handoff. It won't replace static analysis tools or a real code review, and it tends to focus on style over logic bugs.

**What is AI most useful for in optimisation, and what does it fundamentally not know about your system?**

- Most useful for targeted improvements you can describe — restructuring a loop that queries the database per row, or refactoring for readability. It doesn't know where your app is actually slow; it optimizes for what it can see in the code you paste, not your runtime profile.

**Why must you read AI-generated code before accepting it?**

- The model produces plausible code, not verified code. It can hand you confident, well-formatted, completely wrong code with no signal anything is off. You own what you commit — the post-mortem doesn't note "the AI wrote it."

## Responsible AI and Security

**What is the core security concern with pasting content into a public LLM?**

- Public LLMs may retain, log, and use your input for future training. Anything pasted — source code, schemas, credentials, client data — may be permanently exposed with no retrieval mechanism once submitted.

**Is there a remedy once proprietary data has been submitted to a public model?**

- No. There is no retrieval mechanism once data is submitted to a public model. Assume it is retained permanently.

**What is the difference between a public tool like ChatGPT.com and an enterprise API with a data processing agreement?**

- A public tool has terms that may allow retention and training on your input. An enterprise API with a data processing agreement contractually excludes your data from training and defines retention policies. The terms are not the same — treat tool selection as a data classification decision.

**What is the implicit transmission problem with IDE-integrated tools?**

- IDE tools don't just send what you type — they assemble a context window from open tabs, recently viewed files, imported modules, and surrounding code, transmitting it to the server on every request without any explicit action from you. The trust boundary is the entire workspace, not just the prompt box.

**What is the hard rule about credentials, API keys, and customer data in prompts?**

- They never belong in a prompt — on any tool, on any tier. There is no safe way to paste a credential into a chat window and assume it stays private.

**What is a silent failure, and why is it more dangerous than a loud one?**

- A silent failure is code that compiles, tests pass, and the logic is wrong — no obvious error signal. It's more dangerous because it can corrupt production data for weeks before detection, and every downstream system inherits the bad output.

**Why is a test suite written by the same model that wrote the code not a reliable safety net?**

- The same model may write tests that mock away the behavior they're supposed to verify, or assert the wrong thing while still passing. Independent test authorship and human review are needed for real confidence.

**Why must destructive or irreversible operations such as DROP, DELETE, or a schema migration always require human review?**

- An agent can execute these with real side effects before you see them. The blast radius of a mistaken DROP or migration is enormous and often irreversible — these operations should never be delegated without explicit human approval.

**Why should you verify package names independently before installing them?**

- AI regularly invents package names that don't exist. A malicious actor can register those hallucinated names on a package registry, turning a typo into a supply chain attack.

**Who owns the output of a deployed AI system?**

- The organization that deploys it. "The model said it" is not a legal, ethical, or professional defense. You reviewed it and shipped it — you own the outcome.

**Where does bias in an AI model come from?**

- Training data. If historical data reflects past discriminatory practices, skewed sampling, or biased labeling, the model learns to replicate those patterns. The same applies to third-party models — you inherit the vendor's training decisions.

**When selecting a third-party model, what should you review, and what does missing documentation signal?**

- Review the vendor's model card or documentation for how training data was sourced, filtered, and evaluated for bias. Missing documentation is itself a signal — you cannot know what biases you're embedding into your product.

**Why should AI outputs that inform high-stakes decisions have a human escalation path and be kept auditable?**

- If you cannot explain why the model returned a result, you cannot defend it. High-stakes decisions — fraud scoring, credit risk, hiring — need a human who can review, override, and account for the output.

**What is dependency confusion (package hallucination)?**

- When AI suggests a package name that doesn't exist in the registry. If a malicious actor has registered that name, installing it pulls in attacker-controlled code instead of the library you expected.

**Walk through the attack chain that unfolds when a developer installs a hallucinated package.**

- The model suggests a plausible but nonexistent package name. A malicious actor has registered that name on PyPI or npm with harmful code. The developer installs it without checking the registry. The malicious package runs in their environment — potentially exfiltrating credentials, modifying CI/CD pipelines, or compromising the entire build chain.

**What is agentic overreach, and what controls limit it?**

- An AI agent with write or delete access acting beyond its intended scope — modifying production data, running destructive commands, or changing dozens of files unattended. Controls include least privilege, environment separation, gated approval, and requiring human review for irreversible operations.

**What is skill atrophy, and why is it a risk for a development team?**

- Team members losing foundational skills — debugging, reading documentation, reasoning about architecture — because they rely on AI for everything. If the team can't debug without AI assistance, they lose the ability to catch and fix the model's mistakes.

**Why is AI described as a "force multiplier" for engineers who understand the domain?**

- AI amplifies what you already know. Engineers who understand the domain can identify where AI is likely wrong, steer it effectively, and verify its output. Without that foundation, the multiplier has nothing to work on — you're just accepting plausible output blindly.

## Stretch Questions

**What is the difference between narrow (weak) AI and general (strong) AI?**

- Narrow AI is designed for specific tasks — fraud detection, language generation, image classification. General AI would match human-level reasoning across any domain. Every AI system in production today is narrow AI.

**Where does deep learning sit relative to machine learning, and what is a neural network loosely modelled on?**

- Deep learning is a subset of machine learning that uses neural networks with many layers. A neural network is loosely modelled on how neurons in the brain connect and pass signals — layers of nodes that transform input through weighted connections.

**What is reinforcement learning, and how does it differ from supervised and unsupervised learning?**

- Reinforcement learning trains an agent by rewarding desired behavior and penalizing undesired behavior through trial and error, rather than learning from labeled examples (supervised) or finding structure in unlabeled data (unsupervised). Common in game-playing AI and robotics.

**What is the difference between a feature and a label in a supervised learning dataset?**

- Features are the input variables the model uses to make predictions — transaction amount, location, time of day. The label is the correct answer you want the model to predict — "fraud" or "legitimate."

**What is the difference between a classification problem and a regression problem?**

- Classification predicts a category or label — fraud or not, positive or negative sentiment. Regression predicts a continuous number — a dollar amount, a temperature, a probability score.

**What is overfitting, and why is it a problem?**

- Overfitting means the model memorized its training data too closely and performs poorly on new data. It learned noise and specifics of the training set rather than generalizable patterns, defeating the purpose of generalization.

**What is a "foundation model," and why is the term used?**

- A foundation model is a large model trained on broad data (text, code, images) that can be adapted to many downstream tasks through prompting or fine-tuning. The term reflects that it serves as a base layer other applications build on.

**How does a text-generating LLM differ from a generative image model in terms of output and typical use?**

- An LLM generates sequential text token by token — drafting code, summaries, or answers. An image model generates pixels or latent representations — creating illustrations, photos, or diagrams. LLMs are used for language and code tasks; image models for visual content creation.

**What is the transformer architecture, and what key mechanism does it rely on?**

- The transformer is the architecture behind modern LLMs. Its key mechanism is self-attention — each token can weigh the relevance of every other token in the input, allowing the model to capture long-range dependencies in text rather than processing sequentially.

**What does it mean for a model to be "pre-trained," and how does pre-training relate to fine-tuning?**

- Pre-training is the initial large-scale training on broad data that gives the model general language or code ability. Fine-tuning continues training on a smaller, specialized dataset afterward to adapt the pre-trained model to a specific domain or task.

**What are embeddings, and where might they be used in a data product (for example, semantic search)?**

- Embeddings are dense numerical vectors that represent the meaning of text (or other data) in a way that similar content ends up close together in vector space. In semantic search, you embed documents and queries, then find the closest matches — surfacing relevant content even when exact keywords don't match.

**What is Retrieval-Augmented Generation (RAG), and what problem does it solve that a bare LLM cannot?**

- RAG retrieves relevant documents from an external knowledge base and includes them in the prompt before generation. It solves the problem of the model not knowing your proprietary data, current information, or domain-specific facts — it grounds the response in real sources rather than relying solely on training data.

**What is "temperature," and how does it affect a model's output?**

- Temperature controls randomness in token selection. Low temperature makes the model pick the most likely tokens, producing focused, deterministic output. High temperature allows less likely tokens, producing more creative and varied — but potentially less reliable — output.

**How can you make an LLM's responses more deterministic, and when would you want to?**

- Lower the temperature, use a fixed seed where supported, and give explicit format constraints. You'd want deterministic output for production pipelines, automated classification, or any task where consistency matters more than creativity.

**Why might you set a maximum-token limit on a request, and what happens if a response is cut off mid-way?**

- To control cost and response length. If the limit is hit mid-response, the output truncates abruptly — potentially leaving code incomplete, JSON malformed, or an explanation unfinished.

**When would you deliberately choose a smaller, cheaper model over a larger, more capable one?**

- For high-volume, well-defined tasks where a smaller model performs adequately — simple classification, formatting, or extraction. It reduces cost and latency when you don't need the reasoning depth of a frontier model.

**How would you evaluate or benchmark whether a model is good enough for a specific task before shipping it?**

- Define success criteria for your specific task, build a representative test set, run the model against it, and measure accuracy, consistency, and failure modes. Compare against a baseline (smaller model, rule-based approach, or human performance) and test edge cases the model is likely to mishandle.

**What is the difference between a system prompt and a user prompt?**

- A system prompt sets persistent behavior, role, and constraints for the entire conversation — defined by the application, not the end user. A user prompt is the specific request or input from the user in each turn.

**What is the difference between zero-shot, one-shot, and few-shot prompting?**

- Zero-shot provides no examples — just the task description. One-shot provides exactly one worked example. Few-shot provides a small number of examples (typically 2–5) to demonstrate the expected pattern and format.

**How would you prompt a model to return valid, machine-readable JSON, and why must you still validate the result?**

- Explicitly request JSON output, specify the schema or keys you expect, and optionally include a one-shot example of the desired structure. You must still validate because the model can produce malformed JSON, omit fields, or hallucinate values — parsing with a schema validator catches these failures.

**What does asking a model to "think step by step" (chain-of-thought) do, and why can it improve answers?**

- It prompts the model to show its reasoning process before giving a final answer. Breaking a problem into intermediate steps gives the model more tokens to work through the logic, which often improves accuracy on multi-step reasoning, math, and complex decisions.

**Why can breaking a complex task into smaller sequential steps improve a model's output?**

- Each step is a simpler prediction problem with a narrower space of likely continuations. The model can focus on one piece at a time, and earlier steps provide context that steers later steps toward a better final result.

**What is a prompt injection attack, and how does it differ from SQL injection?**

- Prompt injection embeds malicious instructions in user input that override the system's intended behavior — tricking the model into ignoring its constraints. Unlike SQL injection, which exploits query structure in a database, prompt injection exploits the model treating all input as instructions to continue from.

**Why should user input that gets inserted into a prompt be treated as untrusted?**

- Any user input in a prompt can contain instructions designed to override your system prompt or extract hidden context. Treating it as untrusted and sanitizing or separating it from system instructions prevents attackers from hijacking the model's behavior.

**What is the risk of an LLM leaking its system prompt or other hidden context, and how might you mitigate it?**

- An attacker can craft input that tricks the model into revealing its system prompt, internal instructions, or confidential context. Mitigate by not putting secrets in system prompts, filtering output for leaked instructions, using separate system and user message roles, and testing for injection vulnerabilities before deployment.
