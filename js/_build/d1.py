from common import meaning, exam, trap, h2, p, ul, table, q_single, q_multi, q_order, q_match, topic


def topics():
    return [
        topic(
            "d1-stack",
            1,
            "1.1",
            "AI, ML, deep learning, GenAI, agents — the stack",
            "Memorize the nesting. Almost every Domain 1 stem starts here.",
            meaning(
                "These five names sit inside each other. Learn the order. The exam asks which layer a job is.",
                [
                    "<b>AI</b> — software that does work a person used to do: read a picture, read text, or guess a result.",
                    "<b>ML (machine learning)</b> — a type of AI that learns from past data. You do not write every rule. The computer finds the pattern.",
                    "<b>Deep learning</b> — a type of ML that uses a <b>neural network</b> (many layers of math). You do not build one on this exam. You only name it.",
                    "<b>GenAI (generative AI)</b> — AI that <b>writes new</b> text, code, images, audio, or video.",
                    "<b>Agentic AI</b> — GenAI that can also <b>call other systems</b> (an API = a program other software can call) and keep going until the task is finished.",
                ],
                "Support tickets in a company:<br>"
                "1. Past tickets are labeled billing / outage / access. A model learns that pattern and tags a new ticket. That is <b>ML</b>. On AWS this is often <b>SageMaker</b> (you train a model on your data).<br>"
                "2. Another model writes a draft reply in English. That is <b>GenAI</b>. On AWS this is often <b>Bedrock</b> (you call a ready-made large model).<br>"
                "3. The system then calls the orders API, issues the refund, and updates the ticket. That is <b>agentic AI</b>. On AWS this is often a <b>Bedrock agent</b>.",
            )
            + exam(
                "They give a one-line job and ask which <b>layer</b> it is. "
                "“Writes a product description” = generative. "
                "“Groups customers with no labels” = ML (unsupervised), not GenAI. "
                "“Books a refund by calling the payments API after a plan” = agentic. "
                "They also throw definitions: model vs algorithm, training vs inference, NLP vs computer vision, LLM vs foundation model."
            )
            + h2("Terms they expect you to say")
            + table(
                ["Term", "Say this"],
                [
                    ["Model", "The learned artifact that predicts or generates"],
                    ["Algorithm", "The procedure used to train that model"],
                    ["Training", "Learning patterns from data"],
                    ["Inference", "Using the trained model on new data (production)"],
                    ["Neural network", "Layers of nodes that transform inputs into outputs"],
                    ["Computer vision", "AI that understands images or video"],
                    ["NLP", "AI that understands human language"],
                    ["LLM", "A foundation model specialised in text/code"],
                    ["Foundation model (FM)", "Large pre-trained model reused across many tasks"],
                    ["Bias / fairness / fit", "Systematic error / comparable outcomes / how well the model matches the data"],
                ],
            )
            + trap(
                "Do not call a classifier “generative AI.” Classification and regression are traditional ML even if they sit on AWS. "
                "Do not call a chatbot that only answers from one prompt an “agent” unless it uses tools or multi-step plans."
            ),
            [
                q_single(
                    "A CI pipeline uses an LLM to draft a unique release-notes paragraph from the git log. Which layer of the stack is this?",
                    [
                        "Classic unsupervised clustering",
                        "Generative AI (creates new text)",
                        "A rules engine that must be exact",
                        "Computer vision only",
                    ],
                    1,
                    "New original text from an LLM is generative AI.",
                ),
                q_single(
                    "A warehouse robot plans a route, calls a barcode API, then updates inventory until a pallet is put away. What is this pattern?",
                    ["Batch regression", "Agentic AI (plan + tools + act)", "Zero-shot image captioning only", "A Glacier archive job"],
                    1,
                    "Planning, tool use, and acting toward a goal is agentic AI.",
                ),
                q_single(
                    "Which statement matches AWS exam wording?",
                    [
                        "Training is using a finished model on live traffic",
                        "Inference is learning weights from the training set",
                        "A model is the learned artifact; an algorithm is the training procedure",
                        "NLP only means drawing bounding boxes on faces",
                    ],
                    2,
                    "Model = learned artifact. Algorithm = how you train it. Inference = using it.",
                ),
                q_single(
                    "A warehouse app must read handwritten SKU codes from photos of labels. Which capability is that?",
                    ["Time-series forecasting", "Computer vision (and likely OCR)", "Reinforcement learning for chess", "Token pricing"],
                    1,
                    "Understanding images is computer vision. Text-in-image is often Rekognition or Textract on the exam.",
                ),
                q_multi(
                    "A company describes an LLM. Which TWO statements are correct?",
                    [
                        "An LLM is a foundation model specialised in language and code",
                        "Every FM must be trained from scratch on exam day",
                        "FMs are large pre-trained models you adapt instead of starting from zero",
                        "An LLM cannot be used inside an agent",
                        "NLP is only used for credit-card chip manufacturing",
                    ],
                    [0, 2],
                    "LLM ⊂ FM. You adapt FMs; you almost never pre-train from scratch.",
                ),
                q_match(
                    "Match the term to the exam definition.",
                    ["Training", "Inference", "Bias", "Fairness"],
                    [
                        "Using a trained model on new data",
                        "Learning patterns from data",
                        "Comparable outcomes across groups",
                        "Systematic error that favours or harms a group or outcome",
                    ],
                    [1, 0, 3, 2],
                    "Training vs inference is a favourite pair. Bias is error; fairness is comparable outcomes.",
                ),
            ],
        ),
        topic(
            "d1-learn",
            1,
            "1.1",
            "Learning types: supervised, unsupervised, reinforcement",
            "Read the data first: labels? rewards? Then pick the learning type.",
            meaning(
                "Look at the data first. Does each row already have the correct answer? That one fact picks the learning type.",
                [
                    "<b>Supervised</b> — each example already has the answer (a <b>label</b>). Predict a category = classification. Predict a number = regression.",
                    "<b>Unsupervised</b> — no answers on the rows. The model only groups similar rows (clustering) or finds odd rows (anomaly detection).",
                    "<b>Reinforcement</b> — the system tries an action and gets a score (reward). Used for robots and for RLHF (humans pick the better chatbot reply).",
                    "<b>Semi-supervised</b> — a few rows have labels; most do not.",
                    "<b>Self-supervised</b> — the model makes its own labels (hide a word, guess it). This is how large language models are first trained.",
                ],
                "1. Tickets already tagged P1 / P2 / P3 → <b>supervised classification</b>.<br>"
                "2. Network logs with no incident tag; you only want groups of similar traffic → <b>unsupervised clustering</b>.<br>"
                "3. Humans pick the safer of two chatbot replies so the model learns preference → <b>RLHF</b> (reinforcement).",
            )
            + exam(
                "Story always hides the hint: “labeled tickets,” “no labels,” “reward when the robot docks,” “only 2% of rows are tagged.” "
                "They will not ask you to code a loss function. They ask you to <b>name the learning type</b>."
            )
            + table(
                ["Hint in the stem", "Pick"],
                [
                    ["Predict a number", "Regression (supervised)"],
                    ["Predict a named category", "Classification (supervised)"],
                    ["Group with no labels", "Clustering (unsupervised)"],
                    ["Trial and reward", "Reinforcement"],
                    ["Labels are expensive / rare", "Semi-supervised"],
                    ["Predict the next/masked token at huge scale", "Self-supervised (FM pre-train)"],
                ],
            )
            + trap(
                "“Customers with similar behaviour” without named segments = clustering, not classification. "
                "RLHF is reinforcement used to align an LLM — do not pick “unsupervised clustering” for that."
            ),
            [
                q_single(
                    "PCB photos are already tagged “pass / fail / rework.” The team wants a model that labels new photos. Which learning type?",
                    ["Unsupervised clustering", "Supervised classification", "Reinforcement with a dock reward", "Self-supervised video generation only"],
                    1,
                    "Named labels and a category output = supervised classification.",
                ),
                q_single(
                    "VPC flow logs have no incident tags. The team wants natural groups of similar traffic. Which approach?",
                    ["Supervised regression of tax rates", "Unsupervised clustering", "RLHF on a legal brief", "Batch Translate"],
                    1,
                    "No labels + grouping = unsupervised clustering.",
                ),
                q_single(
                    "An autoscaler tries instance sizes and receives a reward when p95 latency and cost both improve. Which learning type?",
                    ["Supervised classification", "Unsupervised clustering", "Reinforcement learning", "Prompt caching"],
                    2,
                    "Actions plus a reward signal = reinforcement learning.",
                ),
                q_single(
                    "A hospital can label only 3% of scans. They train on the tiny labeled set plus a large unlabeled pile. What is this called?",
                    ["Semi-supervised learning", "Pure reinforcement", "Exact payroll rules", "Provisioned Throughput"],
                    0,
                    "Few labels + lots of unlabeled data = semi-supervised.",
                ),
                q_single(
                    "How are most foundation models first trained at huge scale?",
                    [
                        "A human labels every token by hand",
                        "Self-supervised objectives such as next-token or masked-token prediction",
                        "Only reinforcement with no text",
                        "Only SageMaker Model Cards",
                    ],
                    1,
                    "FM pre-training is self-supervised on massive unlabeled text/images.",
                ),
                q_order(
                    "A team moves from raw logs to an RLHF-aligned chatbot. Put these learning ideas in the usual exam order of appearance.",
                    [
                        "Self-supervised pre-training of the foundation model",
                        "Supervised fine-tuning on instruction examples",
                        "Reinforcement learning from human feedback (RLHF)",
                    ],
                    [0, 1, 2],
                    "Pre-train (self-supervised) → optional SFT → optional RLHF.",
                ),
            ],
        ),
        topic(
            "d1-data",
            1,
            "1.1",
            "Data types: labeled, structured, unstructured",
            "The exam uses data shape to push you toward traditional ML or an FM.",
            meaning(
                "The exam looks at the shape of your data. That choice points to classic ML or to a foundation model.",
                [
                    "<b>Labeled</b> — the correct answer is already on the row (fraud / not fraud). <b>Unlabeled</b> — no answer column.",
                    "<b>Structured / tabular</b> — a table: rows and columns. CSV, a warehouse table, or a database item.",
                    "<b>Unstructured</b> — free-form files: text, images, video, audio, PDFs. Often stored in <b>S3</b> (AWS file storage).",
                    "Also named on the guide: <b>time-series</b> (values over time), <b>image</b>, <b>text</b>.",
                ],
                "1. An orders table with a chargeback yes/no column → labeled structured data. Train a model in <b>SageMaker</b>.<br>"
                "2. Three years of PDF contracts in S3, no tags, staff want to ask questions in English → unstructured. Use <b>Bedrock</b> plus a <b>Knowledge Base</b> (the AWS RAG service).",
            )
            + exam(
                "“CSV of sales with a price column” + predict the number = traditional supervised ML. "
                "“10 years of PDFs and emails, no labels” + Q&A = foundation model + RAG. "
                "They ask which data type you have, not how to engineer features."
            )
            + table(
                ["You have", "Exam lean"],
                [
                    ["Labeled tabular", "Classic ML (SageMaker / Canvas)"],
                    ["Unlabeled table, want groups", "Clustering"],
                    ["Unstructured text/images, want generation or flexible Q&A", "FM / GenAI"],
                    ["Time-stamped sensor numbers", "Time-series / forecast-style ML"],
                ],
            )
            + trap(
                "A PDF is unstructured even if it contains a table. Textract can extract the table; that does not make the original file “structured data in a warehouse.”"
            ),
            [
                q_single(
                    "A credit union stores loan decisions as rows with columns for income, score, and approved/denied. What data type is this?",
                    ["Unstructured video", "Labeled structured (tabular) data", "A diffusion checkpoint", "Only embeddings"],
                    1,
                    "Rows, columns, and a known target = labeled structured/tabular.",
                ),
                q_single(
                    "A company has 20 years of scanned contracts in S3 and wants staff to ask questions in plain English. Why is an FM a better first thought than a small tabular classifier?",
                    [
                        "Contracts are unstructured text/images and there is no huge labeled class set",
                        "Scans are already a Redshift star schema",
                        "FMs always guarantee exact box-office totals",
                        "MemoryDB is required for PDFs",
                    ],
                    0,
                    "Unstructured + no labels + Q&A is the FM/RAG story.",
                ),
                q_single(
                    "Hourly tide heights with a “flood / no flood” tag are best described as:",
                    ["Unlabeled images", "Labeled time-series", "A prompt cache", "AgentCore Policy"],
                    1,
                    "Values over time plus a label = labeled time-series.",
                ),
                q_single(
                    "Which statement is true?",
                    [
                        "S3 objects of JPEG photos are structured warehouse tables",
                        "Unstructured data includes text, images, audio, and video",
                        "Labeled always means unsupervised",
                        "Tabular data cannot be used for supervised learning",
                    ],
                    1,
                    "Unstructured = free-form media and language.",
                ),
                q_multi(
                    "Which TWO are unstructured on this exam?",
                    [
                        "A customer-support MP3 recording",
                        "A two-column CSV of SKU and price",
                        "A product photo in S3",
                        "A Redshift fact table of orders",
                        "A DynamoDB item with order_id and total",
                    ],
                    [0, 2],
                    "Audio and photos are unstructured. Tables and key-value items are structured.",
                ),
                q_match(
                    "Match the pile of data to the usual first approach.",
                    ["Labeled CSV of house features and sale price", "Raw emails with no tags, need a summary", "Sensor ticks, no event names, want odd spikes"],
                    ["Unsupervised anomaly detection", "Supervised regression", "Generative / NLP summarisation"],
                    [1, 2, 0],
                    "Labeled number = regression. Free text = GenAI. No labels + oddballs = anomaly detection.",
                ),
            ],
        ),
        topic(
            "d1-infer",
            1,
            "1.1",
            "Inference types: real-time, batch, async, serverless",
            "Who is waiting, and how many rows? That picks the inference style.",
            meaning(
                "<b>Inference</b> means using a finished model on new data (the live / production step). The exam asks: is a person waiting, and how many rows?",
                [
                    "<b>Real-time</b> — someone is waiting now (chat reply, payment fraud check).",
                    "<b>Batch</b> — process a huge pile later (overnight). Nobody is watching a loading screen.",
                    "<b>Asynchronous</b> — the job takes minutes (long video or a 300-page PDF). The caller comes back later.",
                    "<b>Serverless</b> — you do not manage servers. You pay per request. <b>Bedrock on-demand</b> is the usual exam example.",
                ],
                "1. Payment page must get allow/deny in under one second → <b>real-time</b> (often a SageMaker endpoint).<br>"
                "2. Score 12 million yesterday’s logs at 02:00 → <b>batch</b>.<br>"
                "3. Extract text from a 300-page scan; result appears in S3 after 10 minutes → <b>asynchronous</b> (often Textract).<br>"
                "4. A chatbot with unknown traffic and no GPU servers to run → <b>serverless Bedrock</b>.",
            )
            + exam(
                "Circle “customer is on the phone,” “nightly for 40 million rows,” “video takes 8 minutes,” or “traffic is unknown and they refuse to manage instances.”"
            )
            + trap(
                "Batch is not “slow real-time.” If a human is waiting, it is real-time even if the model is small. "
                "Serverless is about ops and billing, not about accuracy."
            ),
            [
                q_single(
                    "A checkout page must accept or decline a card in under a second. Which inference style?",
                    ["Nightly batch on yesterday’s carts", "Real-time inference", "Glacier restore then score", "Offline distillation only"],
                    1,
                    "A waiting customer = real-time.",
                ),
                q_single(
                    "A utility scores 12 million meters every night to plan crews. Nobody watches a UI during the run. Which style?",
                    ["Real-time chat", "Batch inference", "Interactive AgentCore Identity", "One-shot prompting"],
                    1,
                    "Huge volume, no waiter = batch.",
                ),
                q_single(
                    "A documentary studio submits 2-hour films; results appear in a folder 15 minutes later. Which inference type fits best?",
                    ["Synchronous real-time only", "Asynchronous inference", "Must use MemoryDB", "Exact SQL payroll"],
                    1,
                    "Long jobs with later pickup = asynchronous.",
                ),
                q_single(
                    "A startup has spiky chatbot traffic and no ML ops staff. They want to pay per request. What do they want?",
                    ["Self-managed GPU fleet they idle all weekend", "Serverless on-demand inference (for example Bedrock)", "Always-on Provisioned Throughput they do not need", "EMR on reserved hardware only"],
                    1,
                    "Spiky + no servers = serverless / on-demand.",
                ),
                q_multi(
                    "Which TWO statements are correct?",
                    [
                        "Real-time is for interactive user waits",
                        "Batch is ideal when a shopper is mid-checkout",
                        "Async suits long documents or video",
                        "Serverless always trains a new FM from scratch",
                        "Inference means labelling the original training set",
                    ],
                    [0, 2],
                    "Real-time = wait. Async = long job. Batch ≠ checkout.",
                ),
                q_match(
                    "Match the story to the inference type.",
                    ["Voice bot answers now", "Score all invoices at 02:00", "OCR a 400-page scan; email when done", "Unknown chat spikes, no fleet"],
                    ["Batch", "Asynchronous", "Serverless / on-demand", "Real-time"],
                    [3, 0, 1, 2],
                    "Wait / night / later / no servers.",
                ),
            ],
        ),
        topic(
            "d1-when",
            1,
            "1.2",
            "When AI is right — and when it is not",
            "Not every business problem should use a model. This is easy points.",
            meaning(
                "Use AI when data has a pattern a person cannot write as simple rules. Do not use it when the answer must be exact every time.",
                [
                    "<b>Use AI/ML</b> — messy language, images, product recommendations, forecasts, Q&amp;A over documents.",
                    "<b>Do not use GenAI</b> — tax, payroll, or any number that must match a published table every time.",
                    "Skip AI if a SQL query or a simple if/else already works, if the cost is higher than the value, or if you have no data.",
                    "If a regulator asks “why this row?”, use a small traditional model plus <b>SageMaker Clarify</b> (shows which columns mattered). A large language model usually cannot do that.",
                ],
                "1. VAT on an invoice must match the tax table → write code / rules. Do not use Claude or Bedrock.<br>"
                "2. Route messy emails to billing / legal / ops → AI is fine (<b>Comprehend</b> or Bedrock).<br>"
                "3. A credit decline must list which columns caused it → SageMaker + Clarify, not a chatbot.",
            )
            + exam(
                "They plant words like “must be exact,” “statutory formula,” “already a simple IF,” or “no historical data.” "
                "The correct pick is often “use a rules engine / SQL / traditional ML,” not Bedrock."
            )
            + h2("Problem types they mix into this task")
            + ul(
                [
                    "<b>Classification</b> — pick a category (spam / not spam).",
                    "<b>Regression</b> — pick a number (price, minutes).",
                    "<b>Clustering</b> — groups without labels.",
                    "<b>Generation</b> — create new content.",
                ]
            )
            + trap(
                "An LLM that “usually” calculates VAT is still wrong. Exact money and law = rules or classic software."
            ),
            [
                q_single(
                    "Payroll must apply a published tax table with zero creativity. What should they use?",
                    [
                        "A high-temperature multimodal FM",
                        "A deterministic rules / calculation engine, not a generative model",
                        "Unsupervised clustering of payslips",
                        "Nova Reel to invent tax law",
                    ],
                    1,
                    "Guaranteed exact outcomes are not a GenAI job.",
                ),
                q_single(
                    "A shop already filters “orders over $50 ship free” in SQL. They ask if they should replace it with Claude. Best advice?",
                    [
                        "Yes — every IF statement must become an LLM",
                        "No — a simple existing rule does not need AI",
                        "Only if they enable MemoryDB",
                        "Only if temperature is 1.2",
                    ],
                    1,
                    "If a query already solves it, do not force AI.",
                ),
                q_single(
                    "A clinic has no historical labels and no way to collect them, and wants a custom disease classifier next week. What is the blocker?",
                    ["They forgot Polly", "No data (and no path to get it) makes custom supervised ML a poor fit", "They must pick Artifact first", "Batch inference is illegal"],
                    1,
                    "No data → do not promise a custom classifier.",
                ),
                q_single(
                    "A lender must explain each decline to a regulator with feature reasons. They have a small labeled table. Best first direction?",
                    [
                        "A huge black-box FM with no logging",
                        "Traditional supervised ML plus explainability tools (for example Clarify)",
                        "Zero-shot image generation",
                        "Raise temperature for more variety",
                    ],
                    1,
                    "Explainability + tabular labels = classic ML, not a giant FM.",
                ),
                q_multi(
                    "Which TWO are good reasons to skip GenAI?",
                    [
                        "The output must match a statutory formula every time",
                        "Cost per request would exceed the value of the task",
                        "Users want a draft marketing slogan",
                        "Staff want a chatbot over policy PDFs",
                        "They need flexible translation of support email",
                    ],
                    [0, 1],
                    "Exactness and bad ROI kill the GenAI case. The other three are typical GenAI jobs.",
                ),
                q_single(
                    "A city wants unnamed groups of commuters from tap-card logs with no satisfaction scores. Problem type?",
                    ["Regression", "Clustering", "Exact payroll", "Prompt injection"],
                    1,
                    "No labels + groups = clustering.",
                ),
            ],
        ),
        topic(
            "d1-svc",
            1,
            "1.2",
            "AWS AI application services (pick the name)",
            "These are the easiest scored questions if you memorize the job line.",
            meaning(
                "AWS already trained models for common jobs. You do not train these. You pick the service whose name matches the job in the question.",
                [
                    "Circle the verb: speech to text, text to speech, language A to B, faces in a photo, fields from a PDF, chatbot that fills slots, product recommendations.",
                    "If a dedicated service exists, do not pick Bedrock (faces = Rekognition, not Claude).",
                    "<b>SageMaker / Canvas</b> — you train a custom model. <b>JumpStart</b> — one-click ready models.",
                ],
                "1. Call recordings in S3 must become text you can search → <b>Transcribe</b> (speech to text).<br>"
                "2. A scanned invoice must become JSON fields → <b>Textract</b> (read forms/PDFs).<br>"
                "3. A phone bot collects date + account ID to open a ticket → <b>Lex</b> (chatbot).",
            )
            + exam(
                "The stem is almost a dictionary: “speech to text,” “text to speech,” “language A to B,” “faces in a photo,” “forms from a PDF,” “chatbot slots,” “product recommendations.” Circle the verb, pick the brand name."
            )
            + table(
                ["Need", "Service"],
                [
                    ["Sentiment, entities, key phrases, language, PII in text", "Amazon Comprehend"],
                    ["Medical NLP / PHI", "Amazon Comprehend Medical"],
                    ["Objects, faces, celebs, unsafe images, text-in-image", "Amazon Rekognition"],
                    ["Speech → text", "Amazon Transcribe"],
                    ["Text → speech", "Amazon Polly"],
                    ["Language A → language B", "Amazon Translate"],
                    ["Text/tables/forms from PDFs and scans", "Amazon Textract"],
                    ["Chatbot / voice bot with NLU + slots", "Amazon Lex"],
                    ["Classic enterprise search over docs", "Amazon Kendra (or Q / Knowledge Bases if they want generated answers)"],
                    ["Product recommendations", "Amazon Personalize"],
                    ["Time-series forecast (legacy name)", "Amazon Forecast — know the job"],
                    ["No-code ML for analysts", "SageMaker Canvas"],
                    ["Build / train / deploy custom ML", "Amazon SageMaker AI"],
                    ["One-click pre-trained / OSS models", "SageMaker JumpStart"],
                    ["Employee Q&A over company knowledge", "Amazon Q Business / Amazon Quick"],
                    ["Coding assistant / agentic IDE", "Amazon Q Developer / Kiro"],
                    ["Clinical notes from a visit", "Amazon HealthScribe (know it exists)"],
                ],
            )
            + trap(
                "Textract = extract from documents. Translate = languages. Transcribe = speech to text. "
                "Comprehend = understand text you already have. Rekognition = images/video. "
                "Do not pick Bedrock for “detect celebrity faces” — that is Rekognition."
            ),
            [
                q_single(
                    "A contact centre must turn call recordings in S3 into searchable transcripts. Which service?",
                    ["Amazon Polly", "Amazon Transcribe", "Amazon Rekognition", "Amazon Personalize"],
                    1,
                    "Speech → text is Transcribe. Polly is the opposite.",
                ),
                q_single(
                    "An accessibility feature must read on-screen error text aloud. Which service?",
                    ["Amazon Transcribe", "Amazon Polly", "Amazon Textract", "Amazon Forecast"],
                    1,
                    "Text → speech is Polly.",
                ),
                q_single(
                    "A port authority scans handwritten customs forms and needs the table fields in JSON. Which service?",
                    ["Amazon Translate", "Amazon Textract", "Amazon Lex", "Amazon Q Developer"],
                    1,
                    "Forms and tables from scans = Textract.",
                ),
                q_single(
                    "An ecommerce API wants “customers who bought this SKU also bought…” without training a custom model. Which service?",
                    ["Amazon Personalize", "Amazon Inspector", "AWS Artifact", "Amazon Macie"],
                    0,
                    "Recommendations = Personalize.",
                ),
                q_multi(
                    "A helpdesk wants a voice bot that opens a change ticket (date, account ID) and also translates the confirmation into Japanese. Which TWO services fit the jobs?",
                    ["Amazon Lex", "Amazon Translate", "Amazon Inspector", "AWS Trusted Advisor", "Amazon Forecast"],
                    [0, 1],
                    "Lex = chatbot/slots. Translate = language A → B.",
                ),
                q_match(
                    "Match the job to the service.",
                    ["Find faces and unsafe images", "Sentiment in reviews", "Analyst trains ML with no code", "Employee asks HR policy in chat"],
                    ["Amazon Comprehend", "SageMaker Canvas", "Amazon Q Business / Quick", "Amazon Rekognition"],
                    [3, 0, 1, 2],
                    "Vision / NLP / no-code / workplace assistant.",
                ),
            ],
        ),
        topic(
            "d1-trad-fm",
            1,
            "1.2",
            "Traditional ML versus a foundation model",
            "Same business goal, two toolboxes. The constraints pick the box.",
            meaning(
                "Same goal, two toolboxes. The limits in the question pick the box.",
                [
                    "<b>Traditional ML</b> — you train on <b>your</b> table for one job (churn, fraud, price). On AWS this is <b>SageMaker</b> or no-code <b>Canvas</b>.",
                    "Use it when you need a number, or you must show which columns caused the decision.",
                    "<b>Foundation model (FM)</b> — a large model already trained by a vendor. You adapt it with a prompt or RAG. On AWS this is usually <b>Bedrock</b>.",
                    "Use it for language or images, or when you do not have a huge labeled table.",
                    "No ML team, many models, one API → Bedrock. You write training code / own GPUs → SageMaker.",
                ],
                "1. 80,000 labeled loan rows; the bank must show which columns caused a decline → SageMaker + <b>Clarify</b> (explains features).<br>"
                "2. Engineers paste error logs and want a draft runbook; there is no labeled “correct runbook” table → Bedrock.",
            )
            + exam(
                "Look for “must explain to a regulator,” “small CSV,” “need a draft email,” “no data science team,” “PDFs change every week.”"
            )
            + table(
                ["Stem flavour", "Lean"],
                [
                    ["Explainability, tabular, stable labels", "Traditional ML"],
                    ["Language, images, generation, little labeled data", "FM"],
                    ["No ML team + many FMs via one API", "Bedrock"],
                    ["Custom algorithm / own training loop", "SageMaker"],
                ],
            )
            + trap(
                "An FM can do classification in a pinch, but if they demand feature-level reasons, pick classic ML + Clarify, not Claude."
            ),
            [
                q_single(
                    "A bank has 80,000 labeled rows and must show which features drove a decline. What is more appropriate?",
                    [
                        "A high-temperature image FM",
                        "Supervised traditional ML plus an explainability tool",
                        "Zero-shot jokes with no logs",
                        "Amazon Polly only",
                    ],
                    1,
                    "Tabular + explanations = classic ML + Clarify-style tools.",
                ),
                q_single(
                    "A platform team has messy runbooks in S3 and wants a chatbot that drafts incident replies. No labeled “correct reply” dataset. Best first toolbox?",
                    ["Train a linear model on three columns", "A foundation model (prompt / RAG)", "Only Amazon Forecast", "A Glacier vault"],
                    1,
                    "Unstructured + generation + no labels = FM.",
                ),
                q_single(
                    "The stem says “no ML engineers” and “call several FMs through one managed API.” Which platform?",
                    ["Self-managed GPUs on raw EC2 only", "Amazon Bedrock", "Hand-rolled C++ on a laptop", "Amazon Inspector"],
                    1,
                    "Managed multi-FM API = Bedrock.",
                ),
                q_single(
                    "The stem says “custom training code, their own containers, full MLOps notebooks.” Which platform?",
                    ["Amazon Q Business only", "Amazon SageMaker AI", "Amazon Translate", "AWS Artifact"],
                    1,
                    "You own the training loop = SageMaker.",
                ),
                q_multi(
                    "Which TWO push you toward a foundation model?",
                    [
                        "Need original marketing copy from a short brief",
                        "Need a fully explainable credit score from 12 numeric fields",
                        "Need Q&A over changing policy PDFs",
                        "Need a statutory tax table applied exactly",
                        "Need to group unlabeled numbers with k-means",
                    ],
                    [0, 2],
                    "Generation and PDF Q&A are FM/RAG. Credit explainability and tax are not.",
                ),
                q_single(
                    "JumpStart is mentioned because the team wants a one-click open-source model to try. Where does that live?",
                    ["SageMaker JumpStart", "Amazon Macie", "AWS Config", "S3 Glacier Instant Retrieval only"],
                    0,
                    "JumpStart = one-click pre-trained / OSS models on SageMaker.",
                ),
            ],
        ),
        topic(
            "d1-metrics",
            1,
            "1.3",
            "Metrics, underfitting, overfitting",
            "Accuracy lies on rare events. Fit tells you if the model is too simple or too memorised.",
            meaning(
                "These scores tell you if a yes/no model is any good. <b>Accuracy</b> can look great when the rare case is the one you care about.",
                [
                    "<b>Accuracy</b> — correct answers / all answers. If 99% of rows are “normal,” always saying “normal” looks accurate.",
                    "<b>Precision</b> — of the alerts you raised, how many were real. Care when a false alarm is expensive.",
                    "<b>Recall</b> — of the real problems, how many you caught. Care when a miss is expensive.",
                    "<b>F1</b> — one score that balances precision and recall.",
                    "<b>Underfit</b> — bad on old data and new data (model too simple). <b>Overfit</b> — great on old data, bad on new data (it memorised).",
                ],
                "Fraud is 0.2% of payments. A model that always says “not fraud” is about 99.8% accurate and useless.<br>"
                "If missing fraud is worse than extra reviews → raise <b>recall</b>.<br>"
                "If blocking good cards angers customers → protect <b>precision</b>.",
            )
            + exam(
                "Cancer / fraud / avalanche = maximise recall. Spam filter that must not bury real mail = precision. "
                "“99.9% accurate but misses the rare class” = accuracy trap. "
                "Business metrics they also name: cost per user, development cost, customer feedback, ROI."
            )
            + trap(
                "Do not pick BLEU/ROUGE here — those are Domain 3 text-overlap metrics. Domain 1 is classic ML metrics."
            ),
            [
                q_single(
                    "A rare-disease screen must not miss sick patients even if extra healthy people are sent to a follow-up. Which metric?",
                    ["Precision only", "Recall", "BLEU", "Token cache hit rate"],
                    1,
                    "False negatives are costly → recall.",
                ),
                q_single(
                    "A spam filter that drops real invoices would anger finance. Which metric should they protect?",
                    ["Recall of every newsletter", "Precision of the “spam” class (few false positives)", "ROUGE-L only", "Temperature"],
                    1,
                    "False positives are costly → precision.",
                ),
                q_single(
                    "A model is poor on last year’s training tiles and this week’s new tiles. Diagnosis?",
                    ["Overfitting only", "Underfitting (too simple / high bias)", "Perfect fit", "They used Polly"],
                    1,
                    "High error on train and test = underfit.",
                ),
                q_single(
                    "A playlist model is perfect on last decade’s charts and fails on new singles. Diagnosis?",
                    ["Underfitting", "Overfitting (memorised old quirks)", "Missing Artifact", "Need MemoryDB"],
                    1,
                    "Train great, new data poor = overfit.",
                ),
                q_multi(
                    "Why can accuracy look excellent on a 0.2% fraud dataset? Select TWO true ideas.",
                    [
                        "Predicting “not fraud” almost always is still mostly correct",
                        "Accuracy ignores how rare the positive class is",
                        "Accuracy always equals F1",
                        "Accuracy is only used for image watermarks",
                        "Accuracy cannot be computed on tabular data",
                    ],
                    [0, 1],
                    "Imbalance inflates accuracy. Use precision/recall/F1.",
                ),
                q_match(
                    "Match the symptom to the idea.",
                    ["False positives are expensive", "False negatives are expensive", "Need one balanced number", "Train and test both terrible"],
                    ["F1", "Underfitting", "Precision", "Recall"],
                    [2, 3, 0, 1],
                    "Precision / recall / F1 / underfit.",
                ),
            ],
        ),
        topic(
            "d1-life",
            1,
            "1.3",
            "ML lifecycle and MLOps (conceptual)",
            "You will not build the pipeline. You must name the stage and how the model is hosted.",
            meaning(
                "You will not build the pipeline on the exam. You name the step, and you name how users call the model.",
                [
                    "Usual order: <b>collect → explore → prepare → train → evaluate → deploy → monitor → retrain</b>.",
                    "<b>MLOps</b> — keep the process repeatable: watch the live model and retrain when it drifts.",
                    "<b>Managed API</b> — AWS runs it (Bedrock, Q, Rekognition). This is the usual exam answer.",
                    "<b>Self-hosted</b> — you run the server (SageMaker endpoint or your containers).",
                    "Where FMs come from: a vendor model on Bedrock, an open-source model via JumpStart, or you train your own (rare).",
                ],
                "1. A fraud model gets worse after a new product launches → you skipped <b>monitor / retrain</b>.<br>"
                "2. Two people need face detection and have no GPU team → call <b>Rekognition</b> (managed API). Do not train a new vision model.",
            )
            + exam(
                "Ordering questions love the lifecycle. “Accuracy dropped after a holiday promotion” = monitor then retrain, not “buy Artifact.” "
                "“No team to host GPUs” = managed API."
            )
            + trap(
                "You do not implement CI/CD on this exam. If they ask how to get an FM with no ops, pick Bedrock, not “write a training loop.”"
            ),
            [
                q_order(
                    "Put the ML lifecycle stages in the usual exam order after data is collected and explored.",
                    ["Prepare data", "Train", "Evaluate", "Deploy", "Monitor and retrain"],
                    [0, 1, 2, 3, 4],
                    "Prepare → train → evaluate → deploy → monitor/retrain.",
                ),
                q_single(
                    "A fraud model’s precision fell after a new product launched. Which lifecycle stage did they skip or under-do?",
                    ["Only pre-training a new FM from scratch", "Monitoring (and then retraining) in production", "Downloading Artifact PDFs", "Raising temperature"],
                    1,
                    "Drift after launch = monitor + retrain.",
                ),
                q_single(
                    "A security team wants face detection on badge photos with no ML staff. How should the model be consumed?",
                    ["Self-hosted custom CUDA on laptops", "Managed API (Amazon Rekognition)", "Pre-train a vision FM from zero", "Amazon Forecast"],
                    1,
                    "Managed application API is the default.",
                ),
                q_single(
                    "Which source of an FM is almost never the exam’s first recommendation?",
                    ["Use a Bedrock provider model", "Use JumpStart / Bedrock open-source", "Pre-train a new FM from scratch on their tiny corpus", "Use Amazon Nova"],
                    2,
                    "Pre-train from scratch is extreme cost/time.",
                ),
                q_multi(
                    "Which TWO are MLOps ideas named at practitioner depth?",
                    [
                        "Model monitoring and retraining",
                        "Writing custom CUDA kernels in the exam hall",
                        "Production readiness and reducing technical debt",
                        "Implementing TLS from scratch",
                        "Deriving the attention formula by hand",
                    ],
                    [0, 2],
                    "Monitoring, retraining, production readiness — conceptual only.",
                ),
                q_single(
                    "Self-hosted API on this exam usually means:",
                    ["Amazon Q Business only", "A SageMaker endpoint or your own containers", "AWS Artifact", "Amazon Macie"],
                    1,
                    "You own the endpoint = SageMaker / containers.",
                ),
            ],
        ),
        topic(
            "d1-data-aws",
            1,
            "1.3",
            "AWS data, compute, and cost around ML",
            "Leftover official names: you only need the one-line job.",
            meaning(
                "These AWS names appear on the official list. You only match the one-line job. You do not click the console.",
                [
                    "<b>S3</b> — store files and logs. It is <b>not</b> a search-by-meaning database.",
                    "<b>DataBrew</b> — clean a CSV with no code. <b>Glue</b> — move/catalog data. <b>Lake Formation</b> — who can see lake tables. <b>EMR</b> — big Spark jobs. <b>Redshift</b> — SQL warehouse. <b>Data Exchange</b> — buy a third-party dataset.",
                    "<b>Lambda</b> — a short function with no server to manage. <b>EC2</b> — a virtual machine you manage. <b>ECS/EKS</b> — containers. <b>CloudFront</b> — CDN (files closer to users).",
                    "<b>Budgets</b> — alert when spend crosses a line. <b>Cost Explorer</b> — look at past spend.",
                ],
                "1. Analysts must clean a messy CSV before no-code training, no Spark → <b>Glue DataBrew</b>.<br>"
                "2. Policy PDFs sit in S3 and you need “search by meaning” → add embeddings plus OpenSearch / Aurora / a Knowledge Base. S3 alone only stores the files.",
            )
            + table(
                ["Need", "Pick"],
                [
                    ["Object store for docs, training files, invocation logs", "Amazon S3 (not a vector DB)"],
                    ["Cheap long-term archive of old AI logs", "S3 Glacier"],
                    ["ETL / catalog for ML data", "AWS Glue"],
                    ["No-code data cleaning before training", "AWS Glue DataBrew"],
                    ["Who can see data-lake tables", "AWS Lake Formation"],
                    ["Big Spark / Hadoop processing", "Amazon EMR"],
                    ["SQL warehouse on structured data", "Amazon Redshift"],
                    ["Buy / subscribe to a third-party dataset", "AWS Data Exchange"],
                    ["Run a short function without servers", "AWS Lambda"],
                    ["Virtual machines you manage", "Amazon EC2"],
                    ["Containers (you pick ECS or EKS)", "Amazon ECS / Amazon EKS"],
                    ["CDN in front of an app", "Amazon CloudFront"],
                    ["Alerts on spend", "AWS Budgets"],
                    ["Explore historical cost", "AWS Cost Explorer"],
                ],
            )
            + exam(
                "“Clean a CSV with no code” = DataBrew. “Govern the lake” = Lake Formation. “Huge Spark job” = EMR. "
                "“Store PDFs” = S3. “Search by meaning” is <b>not</b> S3 — that is a vector store / Knowledge Bases."
            )
            + trap(
                "S3 holds files. It does not do similarity search by itself. MemoryDB is out of scope as a vector answer."
            ),
            [
                q_single(
                    "Analysts must visually clean messy CSVs before Canvas training, with no Spark code. Which service?",
                    ["AWS Glue DataBrew", "Amazon Inspector", "Amazon Rekognition", "AWS Artifact"],
                    0,
                    "No-code prep = DataBrew.",
                ),
                q_single(
                    "A data lake on S3 needs table-level permissions for two business units. Which service?",
                    ["Amazon Polly", "AWS Lake Formation", "Amazon Lex", "Amazon Personalize"],
                    1,
                    "Lake permissions = Lake Formation.",
                ),
                q_single(
                    "They store policy PDFs in S3 and want semantic RAG. Why is S3 alone not enough?",
                    [
                        "S3 is not a vector database; they still need embeddings + a vector store / Knowledge Bases",
                        "S3 cannot store PDFs",
                        "S3 is only for Glacier locks",
                        "S3 replaces Bedrock",
                    ],
                    0,
                    "S3 = files. RAG needs retrieval over embeddings.",
                ),
                q_single(
                    "They want a third-party weather dataset in their account instead of scraping. Which service?",
                    ["AWS Data Exchange", "Amazon Transcribe", "Amazon A2I", "Amazon HealthScribe"],
                    0,
                    "Third-party datasets = Data Exchange.",
                ),
                q_multi(
                    "Which TWO match the stem correctly?",
                    [
                        "Nightly Spark feature crunch on terabytes → Amazon EMR",
                        "SQL analytics on a structured warehouse → Amazon Redshift",
                        "Celebrity face detect → Amazon Redshift",
                        "Speech to text → Amazon EMR",
                        "Download SOC reports → Amazon EMR",
                    ],
                    [0, 1],
                    "EMR = big processing. Redshift = warehouse SQL.",
                ),
                q_match(
                    "Match the leftover official name to the job.",
                    ["AWS Lambda", "AWS Budgets", "S3 Glacier", "Amazon CloudFront"],
                    ["Alert when AI spend crosses a line", "Short event-driven compute", "CDN at the edge", "Cheap archive of old logs"],
                    [1, 0, 3, 2],
                    "Lambda / Budgets / Glacier / CloudFront.",
                ),
            ],
        ),
    ]
