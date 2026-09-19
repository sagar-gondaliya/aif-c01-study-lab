from common import meaning, exam, trap, h2, p, ul, table, q_single, q_multi, q_order, q_match, topic


def topics():
    return [
        topic(
            "d2-vocab",
            2,
            "2.1",
            "GenAI vocabulary you must say out loud",
            "If you cannot define token, embedding, and context window, Domain 2 will feel random.",
            meaning(
                "These words appear in cost and RAG questions. A <b>token</b> is not the same as a word.",
                [
                    "<b>Token</b> — a small piece of text the model reads or writes. AWS bills and limits use tokens. About 4 letters, or about ¾ of an English word, per token.",
                    "<b>Context window</b> — the maximum tokens of input + output the model can see in one request.",
                    "<b>Embedding</b> — the text turned into a list of numbers that capture meaning. Similar meaning → similar numbers.",
                    "<b>Vector store</b> — a database that searches those numbers (OpenSearch, Aurora, Neptune, RDS PostgreSQL). <b>S3 is not this</b> — S3 only stores files.",
                    "<b>Chunking</b> — cut a long document into smaller pieces so each piece can be stored and found.",
                    "<b>Multimodal</b> — more than one type (text + image). <b>Diffusion</b> — a common way to generate images or video.",
                ],
                "A 200-page runbook cannot be pasted into Claude. That hits the <b>context window</b>.<br>"
                "You split the file (chunk), turn each piece into numbers (embed), store them in OpenSearch or a Bedrock <b>Knowledge Base</b>, then for each question you fetch only the closest pieces.",
            )
            + exam(
                "They swap “words” for “tokens” in cost questions. They ask why two sentences are “close” (embeddings). "
                "They ask why a 200-page PDF cannot be pasted whole (context window → chunk + RAG)."
            )
            + trap(
                "Do not say S3 is a vector database. Do not say one token = one word. Do not confuse embeddings (meaning vectors) with Guardrails (safety filters)."
            ),
            [
                q_single(
                    "Bedrock bills a support bot by how much text goes in and out. What unit is that?",
                    ["Always whole PDF pages only", "Tokens (input and output)", "Only IAM users", "Only SageMaker instance hours"],
                    1,
                    "On-demand GenAI is token-priced.",
                ),
                q_single(
                    "Why can two different sentences still retrieve the same policy chunk?",
                    ["They share an identical byte string only", "Their embeddings are close in meaning space", "CloudTrail hashes them", "Temperature is always 2.0"],
                    1,
                    "Embeddings capture meaning, not exact spelling.",
                ),
                q_single(
                    "A model rejects a pasted 400-page handbook. What limit did they hit?",
                    ["The context window (too many tokens at once)", "AWS Artifact page count", "Macie finding IDs", "Budgets"],
                    0,
                    "Context window = max tokens in + out.",
                ),
                q_single(
                    "A team generates poster art from a text brief. Which model family idea fits?",
                    ["A diffusion-style image generator", "Amazon Forecast only", "Amazon Transcribe only", "AWS Config rules"],
                    0,
                    "Image/video generators are often diffusion models (Nova Canvas / Reel, Stability, etc.).",
                ),
                q_multi(
                    "Which TWO statements about embeddings are true?",
                    [
                        "They are numeric vectors used for similarity search",
                        "They replace IAM for who can call a model",
                        "Chunking helps long documents fit embedding and retrieval",
                        "They are the same as KMS customer-managed keys",
                        "They delete CloudTrail",
                    ],
                    [0, 2],
                    "Embeddings + chunking = RAG retrieval, not security identity.",
                ),
                q_match(
                    "Match the noun to the meaning.",
                    ["Token", "Context window", "Multimodal", "Transformer"],
                    [
                        "Max tokens the model can see at once",
                        "Architecture using self-attention",
                        "Billing/limit chunk of text",
                        "More than one input or output type",
                    ],
                    [2, 0, 3, 1],
                    "Token / window / multimodal / transformer.",
                ),
            ],
        ),
        topic(
            "d2-tokens",
            2,
            "2.1",
            "Token pricing, latency, and prompt caching",
            "New in v1.1. They will ask how tokens change cost and speed.",
            meaning(
                "On Bedrock you usually pay for <b>input tokens</b> (what you send) plus <b>output tokens</b> (what the model writes). Longer text = more money and often slower replies.",
                [
                    "A huge pack of documents or 40 examples on every call raises <b>input</b> cost.",
                    "A high “max output tokens” setting lets the model write a long answer and raises <b>output</b> cost. For yes/no, set a small max.",
                    "A simple FAQ should use a <b>small cheap model</b> (Nova Micro / Haiku-class), not the largest model.",
                    "<b>Prompt caching</b> — AWS gives a discount when the same first part of the prompt is sent again and again.",
                    "<b>Batch</b> — cheaper if you can wait until later. <b>Provisioned Throughput</b> — you reserve capacity for busy 24/7 traffic. Do not buy it for a quiet bot.",
                ],
                "1. A support bot sends the same 8,000-token policy text with every user sentence. The bill jumps because of <b>input tokens</b>. Turn on prompt caching, or fetch only the needed chunks.<br>"
                "2. Do not buy Provisioned Throughput if the bot runs twice a day.",
            )
            + exam(
                "“Bills exploded after they stuffed 40 examples into every call” = input tokens. "
                "“Answers are novels” = max tokens. "
                "“Same 8k system prompt every time” = prompt caching. "
                "“Steady 24/7 load” = consider Provisioned Throughput."
            )
            + trap(
                "Provisioned Throughput is not the default for a sleepy chatbot. Caching is not RAG. Cutting tokens is not the same as Guardrails."
            ),
            [
                q_single(
                    "A bot sends a 12,000-token policy pack with every user sentence. Cost jumped. What is the main driver?",
                    ["Output tokens only", "Repeated large input tokens", "S3 Glacier retrieval fees only", "Textract free tier"],
                    1,
                    "Fat prompts = input-token cost (and latency).",
                ),
                q_single(
                    "They set max output tokens to 4,096 for a “yes/no” classifier. What happens?",
                    ["Input cost falls to zero", "They risk paying for long answers they do not need", "IAM is disabled", "Embeddings vanish"],
                    1,
                    "Cap output length for short jobs.",
                ),
                q_single(
                    "Every call starts with the same 6,000-token brand bible. Which Bedrock feature cuts that repeat cost?",
                    ["Amazon Macie", "Prompt caching", "AWS Artifact", "Amazon Inspector"],
                    1,
                    "Repeated prefix → prompt caching.",
                ),
                q_single(
                    "Overnight they classify 2 million tickets and can wait until morning. Cost-aware choice?",
                    ["Interactive real-time only", "Batch inference", "Provisioned Throughput they idle all day", "Print tickets and mail them"],
                    1,
                    "Wait-friendly volume = batch.",
                ),
                q_multi(
                    "Which TWO reduce GenAI spend without changing the business answer much?",
                    [
                        "Use a smaller/cheaper model for simple tasks",
                        "Always pick the largest premier model",
                        "Cache a stable system prompt",
                        "Raise temperature to 1.5 to save tokens",
                        "Paste the entire lake into every prompt",
                    ],
                    [0, 2],
                    "Right-size the model and cache static prefixes.",
                ),
                q_single(
                    "When is Provisioned Throughput the exam’s better story?",
                    [
                        "A demo that runs twice a month",
                        "Steady high volume that needs reserved capacity",
                        "They only need Artifact PDFs",
                        "They refuse to use AWS",
                    ],
                    1,
                    "Reserved capacity for busy, predictable load.",
                ),
            ],
        ),
        topic(
            "d2-fm-life",
            2,
            "2.1",
            "FM lifecycle and typical GenAI use cases",
            "You select and adapt. You almost never pre-train.",
            meaning(
                "A <b>foundation model (FM)</b> is a large model already trained by a vendor. You pick it and adapt it. You almost never train a new one from zero.",
                [
                    "Full lifecycle on the guide: pick data → pick model → pre-train → optional fine-tune → evaluate → deploy → collect feedback.",
                    "What you actually do on the exam: pick a model → write a prompt and/or add RAG → maybe fine-tune → evaluate.",
                    "Typical jobs: chat, Q&amp;A on docs, short summaries, rewrite, code, images, an agent that calls APIs.",
                    "“Build our own GPT from scratch on our small files” is almost always the wrong answer.",
                ],
                "Shoppers ask “will this SKU ship to this ZIP?” against product PDFs that change every week.<br>"
                "1. Pick a model on <b>Bedrock</b>.<br>"
                "2. Put the PDFs in a <b>Knowledge Base</b> (RAG = fetch the right page, then answer).<br>"
                "3. Check answers, then use thumbs-down feedback to improve.<br>"
                "Do not pre-train a new FM.",
            )
            + exam(
                "If they describe “teach the model a whole new internet of data from zero,” that is pre-train — almost always the wrong recommendation. "
                "If they describe “draft / summarise / answer from docs,” that is a standard GenAI use case."
            )
            + trap(
                "Fine-tuning is not the first step. Prompt and RAG come first on the cost ladder (Domain 3)."
            ),
            [
                q_order(
                    "Put these FM lifecycle ideas in the usual order for a team that will not pre-train.",
                    ["Select a foundation model", "Prompt / RAG / optional fine-tune", "Evaluate quality and risk", "Deploy and collect feedback"],
                    [0, 1, 2, 3],
                    "Select → adapt → evaluate → deploy/feedback.",
                ),
                q_single(
                    "An SRE team wants one-paragraph summaries of 20-page incident reports. This is mainly which GenAI use case?",
                    ["Time-series forecasting", "Summarisation", "Face liveness", "Cost Explorer"],
                    1,
                    "Long → short text is summarisation.",
                ),
                q_single(
                    "A retailer wants shoppers to ask “will this tent fit three adults?” against product PDFs. Best high-level pattern?",
                    ["Pre-train a new FM on tents from scratch", "GenAI Q&A grounded with RAG", "Only Amazon Forecast", "Rekognition celebrity"],
                    1,
                    "Doc Q&A = RAG + FM, not pre-train.",
                ),
                q_single(
                    "Which step will an AIF-C01 candidate almost never be told to do first?",
                    ["Pick Nova or Claude on Bedrock", "Write a prompt", "Pre-train a new foundation model from scratch", "Turn on evaluation"],
                    2,
                    "Pre-train is the expensive last resort.",
                ),
                q_multi(
                    "Which TWO are typical GenAI use cases on this exam?",
                    [
                        "Draft a product description from bullets",
                        "Apply a statutory tax table with zero variance",
                        "Generate a first-pass image for a campaign",
                        "Guarantee a payroll total",
                        "Replace IAM with a poem",
                    ],
                    [0, 2],
                    "Drafting and images are GenAI. Exact money is not.",
                ),
                q_single(
                    "After launch, users mark answers as unhelpful. Which lifecycle idea is that?",
                    ["Ignore them and pre-train", "Feedback used to improve prompts, RAG, or the model choice", "Delete CloudTrail", "Disable Guardrails forever"],
                    1,
                    "Feedback closes the loop.",
                ),
            ],
        ),
        topic(
            "d2-context",
            2,
            "2.1",
            "Context engineering (not only prompt engineering)",
            "v1.1 added this. The window is a backpack — you choose what goes in.",
            meaning(
                "<b>Prompt engineering</b> is how you write the instruction. <b>Context engineering</b> is everything you put into one request, not only that sentence.",
                [
                    "<b>Prompt engineering</b> — the instruction and any examples you type.",
                    "<b>Context engineering</b> — the instruction + the user question + retrieved document pieces + API results + chat history + the output format you asked for.",
                    "A perfect sentence still fails if you attach the wrong PDF pieces or 60 extra pieces.",
                    "Do not “fix” this by only raising temperature (that only makes wording more random).",
                ],
                "The bot has a clear instruction, but every call also dumps 60 unrelated Knowledge Base pieces. Answers wander.<br>"
                "Keep only the top matching pieces, plus the last few chat turns. That is context engineering.",
            )
            + exam(
                "“Answers ignore the new price list we uploaded” is often retrieval/context, not “the model is dumb.” "
                "“The model forgot the user’s city from two turns ago” is memory / history in the window."
            )
            + trap(
                "Do not “fix” a context problem by only raising temperature. Do not paste the whole lake — that blows tokens and quality."
            ),
            [
                q_single(
                    "A bot has a beautiful system prompt but stuffs 60 unrelated chunks into every call. Answers wander. What discipline is missing?",
                    ["Context engineering (what you put in the window)", "Buying Artifact", "Turning off IAM", "Using MemoryDB"],
                    0,
                    "Wrong or bloated context, not just wording.",
                ),
                q_single(
                    "Which item is part of context engineering beyond the user sentence?",
                    ["Retrieved Knowledge Base passages and tool outputs", "The colour of the laptop", "The exam pass mark", "S3 Glacier vault lock only"],
                    0,
                    "Docs, tools, memory, history all sit in the window.",
                ),
                q_single(
                    "Users say the bot “forgot” their cabin number from the previous turn. What should you inspect first?",
                    ["Whether conversation history / memory is passed into context", "Whether Rekognition can see cabins", "Whether Budgets is on", "Whether Translate is in sa-east-1"],
                    0,
                    "Short-term memory is context.",
                ),
                q_single(
                    "Why is context engineering not the same as fine-tuning?",
                    [
                        "Context is assembled at request time; fine-tuning changes weights",
                        "Fine-tuning never needs data",
                        "Context engineering trains a new FM from scratch",
                        "They are identical AWS services",
                    ],
                    0,
                    "Window vs weights.",
                ),
                q_multi(
                    "Which TWO belong in a well-engineered context for a support agent?",
                    [
                        "A short system role and output format",
                        "The top relevant policy chunks only",
                        "Every email the company ever sent",
                        "KMS key IDs pasted as secrets in the prompt",
                        "The entire S3 bucket as raw bytes",
                    ],
                    [0, 1],
                    "Tight instructions + relevant retrieval. Not the whole universe or secrets.",
                ),
                q_single(
                    "A retrieved chunk is correct but the model still ignores it. Next lever (still in this topic’s spirit)?",
                    [
                        "Put the evidence closer / instruct “answer only from the passages” (and later check temperature / model)",
                        "Delete the vector store",
                        "Switch to payroll rules",
                        "Enable MemoryDB",
                    ],
                    0,
                    "If retrieval is right, generation/prompt/context layout is next (Domain 3 trap too).",
                ),
            ],
        ),
        topic(
            "d2-agents",
            2,
            "2.1",
            "Agentic AI, tools, memory, MCP",
            "An agent does not only answer. It plans, acts, and comes back.",
            meaning(
                "An <b>agent</b> does not only chat. It plans steps, calls other systems, reads the result, and continues until the job is finished.",
                [
                    "<b>Tool / API</b> — another program the agent can call (Jira, a database, <b>Lambda</b> = a short AWS function).",
                    "<b>Short-term memory</b> — this chat only. <b>Long-term memory</b> — remembered next week.",
                    "<b>MCP</b> — a standard way to plug tools into an agent. You only need the name, not the code.",
                    "<b>Strands</b> — a framework for several specialist agents. <b>AgentCore</b> — AWS runtime to run custom agents.",
                    "Use an agent when the next step depends on the question. Use a fixed workflow when every file always follows the same steps.",
                ],
                "1. A bot must choose among Jira, CloudWatch, or ServiceNow, then open a ticket → <b>agent</b> (Bedrock Agents / AgentCore).<br>"
                "2. Every night: Textract reads a PDF → Translate → save in Redshift, always in that order → <b>workflow</b>, not an agent.",
            )
            + table(
                ["Use an agent when…", "Use a fixed workflow when…"],
                [
                    ["Steps depend on the question", "Steps are always the same"],
                    ["Must pick among many tools", "Pipeline is extract → transform → store"],
                    ["Open-ended research / support", "Batch jobs, approvals, retries"],
                ],
            )
            + exam(
                "“Unknown path, many APIs, keep going until booked” = agent. "
                "“Every night: extract → translate → store” = workflow, not an agent. "
                "MCP appears as the <b>standard connector</b>, not as interceptor code you write."
            )
            + trap(
                "Amazon Q / Kiro are productised assistants. AgentCore is what you use when <b>you build</b> custom agents. Do not implement MCP interceptors — that is Professional-level, not AIF-C01."
            ),
            [
                q_single(
                    "An ops bot must choose among Jira, CloudWatch, and ServiceNow APIs depending on the question, then open the ticket. What pattern?",
                    ["A single nightly Glue job with no decisions", "An agent with tool use", "Amazon Forecast only", "S3 Glacier"],
                    1,
                    "Unknown steps + tools = agent.",
                ),
                q_single(
                    "Every invoice follows extract → Textract → Redshift. No branching. Best pattern?",
                    ["An open-ended multi-agent debate", "A fixed workflow / pipeline", "RLHF on each invoice", "Kiro for the warehouse"],
                    1,
                    "Same steps every time = workflow.",
                ),
                q_single(
                    "What is MCP on this exam?",
                    [
                        "A standard way to connect agents to tools and data",
                        "A replacement for IAM users",
                        "A vector database that replaced OpenSearch",
                        "An encryption algorithm you implement",
                    ],
                    0,
                    "MCP = tool/data connector standard.",
                ),
                q_single(
                    "A user returns next week and the bot still knows their boat name. What kind of memory is that?",
                    ["Short-term / session only", "Long-term memory across sessions", "Prompt caching of KMS keys", "Batch inference"],
                    1,
                    "Across sessions = long-term memory.",
                ),
                q_multi(
                    "Which TWO are true?",
                    [
                        "Strands is a multi-agent framework name in the 2026 guide",
                        "AgentCore is for teams building custom production agents",
                        "MCP means you must write hypervisor firmware",
                        "Every ETL job must be an agent",
                        "Q Business is only a vector database",
                    ],
                    [0, 1],
                    "Strands + AgentCore are the 2026 agent story.",
                ),
                q_match(
                    "Match the noun.",
                    ["Tool / function calling", "Short-term memory", "MCP", "Orchestration"],
                    ["Session chat / scratchpad", "The control loop that runs the agent", "APIs and actions the agent can invoke", "Standard hook-up to external tools/data"],
                    [2, 0, 3, 1],
                    "Tools / session / MCP / orchestration.",
                ),
            ],
        ),
        topic(
            "d2-limits",
            2,
            "2.2",
            "Strengths, limits, and how to pick a model",
            "Task 2.2 is honest about what GenAI cannot do.",
            meaning(
                "GenAI is good at language and fast to try. It is not always correct, not fully explainable, and not always up to date.",
                [
                    "<b>Strengths</b> — writes text, talks in a conversation, works with little labeled data.",
                    "<b>Hallucination</b> — the text looks confident but is wrong (a fake ticket ID).",
                    "<b>Nondeterminism</b> — the same question can get different wording. Worse if <b>temperature</b> (randomness) is high.",
                    "<b>Weak interpretability</b> — you cannot easily say why it chose those words.",
                    "<b>Stale knowledge</b> — it only knows up to its training date unless you add RAG or a live API.",
                    "Also watch IP, privacy, and bias. Pick a model by: type (text/image), quality, speed, cost, language, compliance.",
                ],
                "1. An IAM bot invents an API action that does not exist → <b>hallucination</b>.<br>"
                "2. Same prompt at temperature 0.9 returns three different JSON shapes → <b>nondeterminism</b>.<br>"
                "3. Training ended last year; you need this week’s EC2 prices → add RAG or a pricing API. A bigger model alone does not fix that.",
            )
            + h2("How they want you to choose a model")
            + p(
                "Score the story on: <b>modality, quality, latency, cost, context length, language, customisation, compliance, complexity</b>."
            )
            + table(
                ["Amazon Nova idea", "Use"],
                [
                    ["Micro", "Cheapest / fastest text"],
                    ["Lite / Pro", "Multimodal, balanced"],
                    ["Premier", "Hardest reasoning / teacher"],
                    ["Canvas / Reel / Sonic", "Image / video / speech"],
                ],
            )
            + p(
                "Also recognise Bedrock providers: Anthropic Claude, Meta Llama, Cohere, Mistral, AI21, Stability AI, plus older Titan mentions (embeddings / image watermarking)."
            )
            + exam(
                "“Must be deterministic and explainable” → not a creative FM. "
                "“Need images + low cost” → smaller multimodal, not Premier. "
                "“Knowledge after the cutoff” → RAG or tools, not a bigger model alone."
            )
            + trap(
                "A larger model does not fix stale facts. High temperature does not add citations. Nova names are about fit, not memorising every SKU."
            ),
            [
                q_single(
                    "A legal bot invents a case citation that does not exist. What limit is this?",
                    ["Hallucination", "Perfect grounding", "Batch inference", "Prompt caching"],
                    0,
                    "Fluent but false = hallucination.",
                ),
                q_single(
                    "The same prompt returns three different wordings at temperature 0.9. What limit?",
                    ["Nondeterminism", "Lake Formation deny", "Exact SQL", "Macie findings"],
                    0,
                    "High temperature + sampling = variation.",
                ),
                q_single(
                    "A model’s training cutoff is last year; they need this week’s EC2 prices. What do they add?",
                    ["Only raise temperature", "RAG or a live tool, not a bigger stale model alone", "Delete Guardrails", "Use Glacier"],
                    1,
                    "Stale knowledge → retrieve or tool.",
                ),
                q_single(
                    "They need cheap, fast replies to “open / closed” FAQ. Which Nova idea?",
                    ["Premier video teacher", "Nova Micro-class (small text)", "Reel for every FAQ", "Sonic for spreadsheets"],
                    1,
                    "Simple text → smallest/cheapest.",
                ),
                q_multi(
                    "Which TWO are GenAI limits the exam expects?",
                    [
                        "Weak interpretability of why a token was chosen",
                        "Always 100% deterministic at any temperature",
                        "IP, privacy, and bias risk",
                        "It can never draft an email",
                        "It always replaces IAM",
                    ],
                    [0, 2],
                    "Explainability + legal/privacy/bias are named limits.",
                ),
                q_match(
                    "Match the selection knob.",
                    ["Need a poster from a sentence", "Need lowest text latency", "Need hardest reasoning", "Need a non-Amazon chat FM"],
                    ["Nova Micro-class", "Claude / Llama / others on Bedrock", "Image / Canvas-class model", "Premier-class"],
                    [2, 0, 3, 1],
                    "Modality / cost / difficulty / provider.",
                ),
            ],
        ),
        topic(
            "d2-biz",
            2,
            "2.2",
            "Business metrics for GenAI",
            "They ask whether the project is worth it — not only BLEU.",
            meaning(
                "A high text score (ROUGE/BLEU) does not mean the project is worth the money. The exam also asks business numbers.",
                [
                    "<b>ROI</b> — did we save more money than we spent?",
                    "<b>Cost per interaction</b> — what one chat costs.",
                    "<b>CSAT / task completion</b> — was the user happy, and was the ticket actually solved?",
                    "<b>ARPU / CLV / conversion</b> — revenue per user, long-term value, did they buy or sign up?",
                    "Judge the <b>whole app</b> (search + prompt + tools), not only the raw model.",
                ],
                "1. Finance asks if a Knowledge Base bot saves more support hours than it costs → <b>ROI</b>, not BLEU (BLEU is a translation score).<br>"
                "2. Users leave after one message and the ticket is still open → low <b>task completion</b> and CSAT.",
            )
            + exam(
                "“Leadership wants to know if the bot pays for itself” = ROI / cost per interaction, not BLEU. "
                "“Users abandon after one turn” = satisfaction / completion, not token cache."
            )
            + trap(
                "Do not answer a CFO question with ROUGE. Do not answer a summarisation-quality question with ARPU."
            ),
            [
                q_single(
                    "Finance asks whether a knowledge bot saves more money than it costs each quarter. Which metric family?",
                    ["ROI / cost per interaction", "BLEU only", "Rekognition face count", "Inspector CVEs"],
                    0,
                    "Payback is a business metric.",
                ),
                q_single(
                    "Support wants to know if tickets are actually resolved in the chat. Which metric?",
                    ["Task completion (and CSAT)", "Token temperature", "Glacier restore time", "JumpStart stars"],
                    0,
                    "Did the job finish for the user?",
                ),
                q_single(
                    "Marketing asks if the image generator increases spend per active shopper. Closest named idea?",
                    ["ARPU (or similar revenue per user)", "ROUGE-1", "Lake Formation LF-Tags only", "HealthScribe"],
                    0,
                    "Revenue per user is a business metric they will accept.",
                ),
                q_single(
                    "A GenAI rewrite tool is loved in a pilot but costs $4 to save $0.20 of staff time. What should you report?",
                    ["Negative or poor ROI — do not scale yet", "Mandatory pre-train", "Disable CloudTrail", "It must be Claude Premier"],
                    0,
                    "Cost/benefit can kill the use case (Domain 1 + 2).",
                ),
                q_multi(
                    "Which TWO are business/application metrics rather than n-gram overlap?",
                    [
                        "Customer satisfaction",
                        "Cost per conversation",
                        "BLEU",
                        "ROUGE",
                        "BERTScore",
                    ],
                    [0, 1],
                    "CSAT and cost are business. BLEU/ROUGE/BERTScore are text metrics (Domain 3).",
                ),
                q_single(
                    "Why evaluate the whole application, not only the raw FM?",
                    [
                        "A great model with bad retrieval or tools still fails the user",
                        "FMs never hallucinate if ROUGE is 1.0",
                        "Business metrics are illegal on AWS",
                        "Bedrock cannot be evaluated",
                    ],
                    0,
                    "App = model + RAG + prompts + tools + UX.",
                ),
            ],
        ),
        topic(
            "d2-platform",
            2,
            "2.3",
            "AWS GenAI platform map",
            "Task 2.3 is “which AWS door do I open?” This is high yield.",
            meaning(
                "This task is only: which AWS product do you open? Your data and IAM stay in your account.",
                [
                    "<b>Bedrock</b> — many large models, one API, AWS runs the servers. Your prompts are not used to train the vendor’s base model.",
                    "<b>SageMaker AI</b> — you train or host your own model. <b>JumpStart</b> — one-click ready / open-source models.",
                    "<b>Q Business / Quick</b> — staff ask questions over company docs. <b>Q Developer / Kiro</b> — help write code.",
                    "<b>Bedrock Agents + AgentCore</b> — you build a custom agent. <b>Strands</b> — several agents together. <b>Transform</b> — modernize old code.",
                    "No ML team → Bedrock. You need custom training and notebooks → SageMaker.",
                ],
                "1. Two people want Claude and Llama, no GPU servers → <b>Bedrock</b>.<br>"
                "2. Data scientists need notebooks and custom training → <b>SageMaker</b>.<br>"
                "3. Staff ask HR questions over Confluence with their existing logins → <b>Q Business / Quick</b>.",
            )
            + table(
                ["You want", "Pick"],
                [
                    ["Many FMs, one API, no servers", "Amazon Bedrock"],
                    ["Train/host your own model, notebooks, MLOps", "SageMaker AI"],
                    ["One-click OSS / pre-trained", "SageMaker JumpStart"],
                    ["Employee assistant over company docs / SaaS", "Amazon Q Business or Amazon Quick"],
                    ["Developer / console coding help", "Amazon Q Developer"],
                    ["Agentic IDE (newer direction)", "Kiro"],
                    ["Build custom agents", "Bedrock Agents + AgentCore"],
                    ["Multi-agent code framework", "Strands Agents"],
                    ["Modernize old codebases", "AWS Transform"],
                ],
            )
            + exam(
                "“No ML team / fastest FM” → Bedrock. “Custom algorithm / own GPUs / not on Bedrock” → SageMaker. "
                "“Staff already have Microsoft/Slack sources and permissions” → Q Business / Quick. "
                "“We are building an agent platform” → AgentCore, not Q."
            )
            + p(
                "Cost tradeoffs they name: responsiveness, availability, redundancy, performance, regional coverage, token pricing, provisioned throughput, custom models."
            )
            + trap(
                "Q is a product. AgentCore is a build platform. JumpStart is not Knowledge Bases. Transform is modernization, not Rekognition."
            ),
            [
                q_single(
                    "A two-person startup wants Claude and Llama through one managed API with no GPUs. Which service?",
                    ["Amazon Bedrock", "Self-managed EC2 only", "Amazon Macie", "AWS Artifact"],
                    0,
                    "Serverless FMs = Bedrock.",
                ),
                q_single(
                    "Data scientists need notebooks, custom training, and their own endpoints. Which service?",
                    ["Amazon Q Business", "Amazon SageMaker AI", "Amazon Polly", "Amazon Translate"],
                    1,
                    "Full ML platform = SageMaker.",
                ),
                q_single(
                    "Employees must ask HR and wiki questions with existing app permissions. First product to consider?",
                    ["Amazon Q Business or Amazon Quick", "Amazon Inspector", "Amazon Forecast", "AWS Data Exchange"],
                    0,
                    "Workplace assistant = Q / Quick.",
                ),
                q_single(
                    "Developers want in-IDE coding help on AWS APIs. Which pair of names is in scope?",
                    ["Amazon Q Developer / Kiro", "Amazon Macie / Inspector only", "Amazon Textract / Polly", "Trusted Advisor / Budgets only"],
                    0,
                    "Coding assistants = Q Developer and Kiro.",
                ),
                q_multi(
                    "Which TWO statements match exam facts?",
                    [
                        "Bedrock does not use your prompts to train the provider’s base models",
                        "SageMaker is the lowest-ops way to call Claude",
                        "AWS Transform is aimed at code/app modernization",
                        "MemoryDB is the required vector store in 2026",
                        "Strands is a face-detection API",
                    ],
                    [0, 2],
                    "Data-use fact + Transform. MemoryDB is out. SageMaker is more ops, not less.",
                ),
                q_match(
                    "Match the door.",
                    ["Bedrock Agents + AgentCore", "SageMaker JumpStart", "Strands Agents", "Amazon Q Business"],
                    ["One-click OSS / pre-trained models", "Employee Q&A product", "You build custom production agents", "Multi-agent framework"],
                    [2, 0, 3, 1],
                    "Build vs click vs framework vs product.",
                ),
            ],
        ),
    ]
