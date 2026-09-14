window.AIF = window.AIF || {};
window.AIF.mocks = window.AIF.mocks || {};
window.AIF.mocks[3] = [
  {
    id: "m3q01",
    domain: 1,
    type: "single",
    stem: "An airline wants a system that writes new delay announcements in several tones from a short brief. Which layer of the AI stack is this, compared with a classifier that only labels tweets as delayed or on time?",
    choices: [
      "It is generative AI because it creates new text, not only a label",
      "It is clustering because sentences have spaces",
      "It is reinforcement learning only if the plane is on the ground",
      "It cannot be AI if Amazon Bedrock is used"
    ],
    answer: [0],
    explain: "Generating novel wording is generative AI. A delay/on-time labeler is discriminative classification."
  },
  {
    id: "m3q02",
    domain: 1,
    type: "single",
    stem: "An insurer wants to predict next quarter's claim amount in dollars from structured policy features. Which task?",
    choices: [
      "Classification of claim fraud yes/no only",
      "Regression of a numeric amount",
      "Unsupervised clustering of photos",
      "Agentic tool use"
    ],
    answer: [1],
    explain: "A dollar amount is regression. Fraud yes/no would be classification; both can be supervised."
  },
  {
    id: "m3q03",
    domain: 1,
    type: "single",
    stem: "A university IR team has unlabeled clickstreams and wants to find unusual exam-period traffic spikes. Which approach is typical?",
    choices: [
      "Supervised regression of tuition fees",
      "Unsupervised anomaly detection or clustering-style outliers",
      "RLHF on every HTTP 200",
      "Amazon Polly pronunciation lexicons"
    ],
    answer: [1],
    explain: "No labels and a hunt for unusual groups or points is unsupervised (often anomaly detection)."
  },
  {
    id: "m3q04",
    domain: 1,
    type: "single",
    stem: "Missing a true cancer flag is far worse than an extra radiologist review. Which metric should the hospital optimise?",
    choices: [
      "Precision only, ignoring missed cases",
      "Recall (catch actual positives)",
      "BLEU on discharge poems",
      "Top-p"
    ],
    answer: [1],
    explain: "Costly false negatives call for recall. Precision fights extra false alarms."
  },
  {
    id: "m3q05",
    domain: 1,
    type: "single",
    stem: "An airline wants one score that balances precision and recall for a baggage-delay alert model. Which metric?",
    choices: [
      "F1 score",
      "Context window",
      "ROUGE-L only",
      "Provisioned Throughput hours"
    ],
    answer: [0],
    explain: "F1 is the harmonic mean of precision and recall. It is a classic ML metric, not a GenAI overlap score."
  },
  {
    id: "m3q06",
    domain: 1,
    type: "single",
    stem: "Passengers upload hour-long complaint videos. Scoring takes minutes and the app emails results later. Which inference pattern?",
    choices: [
      "Synchronous checkout-style real-time only",
      "Asynchronous inference",
      "Nightly batch of a fixed 20 million rows with no per-user job",
      "On-device reinforcement learning"
    ],
    answer: [1],
    explain: "Long jobs where the caller collects the result later are asynchronous. Batch is a scheduled bulk score; real-time is interactive."
  },
  {
    id: "m3q07",
    domain: 1,
    type: "single",
    stem: "An insurer's pricing team has a stable, labeled tabular history and a regulator who will ask why a premium moved. Should they start with a large multimodal FM?",
    choices: [
      "Yes, because FMs always explain coefficients",
      "No: prefer traditional supervised ML when explainability and tabular labels dominate",
      "Yes, with temperature 1.2",
      "Only if they disable CloudTrail"
    ],
    answer: [1],
    explain: "Traditional ML plus Clarify-style tools fit regulated numeric tabular problems. FMs are weaker on why-this-score."
  },
  {
    id: "m3q08",
    domain: 1,
    type: "multi",
    stem: "A university wants click-to-play campus maps and also product-like course recommendations for returning alumni. Which TWO AWS services fit?",
    choices: [
      "Amazon Rekognition to detect landmarks in uploaded campus photos",
      "Amazon Personalize for recommendations",
      "Amazon Forecast as the only vision API",
      "AWS Artifact as the recommender",
      "Amazon Inspector as the campus map"
    ],
    answer: [0, 1],
    explain: "Rekognition is vision; Personalize is recommendations. Artifact and Inspector are compliance and vulnerability tools."
  },
  {
    id: "m3q09",
    domain: 1,
    type: "order",
    stem: "Order inference styles from 'user is blocked on the answer' to 'score a warehouse of files overnight'.",
    items: [
      "Real-time synchronous",
      "Asynchronous job the client polls later",
      "Serverless on-demand for spiky chat",
      "Scheduled batch over millions of rows"
    ],
    answer: [0, 1, 2, 3],
    explain: "Real-time waits. Async returns later. Serverless suits unpredictable chat. Batch is the nightly bulk job. (Serverless can also be real-time; here it sits as the managed spiky option.)"
  },
  {
    id: "m3q10",
    domain: 1,
    type: "match",
    stem: "Match each airline operations need to the service.",
    left: [
      "Enterprise search over old maintenance manuals (no generation)",
      "No-code delay predictor for analysts",
      "Build and host a custom remaining-useful-life model"
    ],
    right: [
      "SageMaker Canvas",
      "Amazon SageMaker AI",
      "Amazon Kendra",
      "Amazon Polly"
    ],
    answer: [2, 0, 1],
    explain: "Kendra is classic enterprise search. Canvas is no-code. SageMaker AI is the full ML platform."
  },
  {
    id: "m3q11",
    domain: 2,
    type: "single",
    stem: "An insurer notices latency and cost climb when few-shot prompts include twelve long claim letters. What is the main driver?",
    choices: [
      "Extra input tokens in the context window",
      "Amazon Inspector package count",
      "The number of IAM password policies",
      "CloudFront SSL certificate days"
    ],
    answer: [0],
    explain: "Few-shot examples occupy input tokens. That raises cost and can slow the call as the window fills."
  },
  {
    id: "m3q12",
    domain: 2,
    type: "single",
    stem: "A university chatbot must remember a student's preferred name across sessions, not only inside one browser tab. What agent memory distinction is this?",
    choices: [
      "Short-term session memory versus long-term memory",
      "BLEU versus ROUGE",
      "Batch versus real-time only",
      "Macie versus Inspector"
    ],
    answer: [0],
    explain: "Session memory dies with the conversation. Long-term memory persists preferences across sessions (AgentCore Memory is the AWS noun)."
  },
  {
    id: "m3q13",
    domain: 2,
    type: "single",
    stem: "Claims processing is always extract fields, then validate, then store. Steps never change with the question. Should they build an open-ended agent?",
    choices: [
      "Yes, agents are always better than workflows",
      "No: a fixed workflow is enough when the path is always the same",
      "Only if they use high temperature",
      "Only if they delete Guardrails"
    ],
    answer: [1],
    explain: "Use an agent when steps and tools depend on the goal. Use a fixed workflow for a stable pipeline."
  },
  {
    id: "m3q14",
    domain: 2,
    type: "single",
    stem: "A carrier wants one API that can reach Claude, Llama, and Amazon Nova without standing up GPUs. Which service?",
    choices: [
      "Amazon Bedrock",
      "Amazon Comprehend Medical only",
      "AWS Artifact",
      "Amazon Macie"
    ],
    answer: [0],
    explain: "Bedrock exposes multiple provider FMs as a managed API. The others are NLP, compliance, or S3 PII discovery."
  },
  {
    id: "m3q15",
    domain: 2,
    type: "single",
    stem: "Faculty want an employee assistant over the LMS, SharePoint, and ticket system that already honours existing permissions. Which product family?",
    choices: [
      "Amazon Q Business or Amazon Quick",
      "Amazon Forecast",
      "Amazon Rekognition celebrity",
      "AWS Snowcone as the LLM"
    ],
    answer: [0],
    explain: "Q Business / Quick is the workplace assistant over enterprise sources. It is not a forecasting or vision API."
  },
  {
    id: "m3q16",
    domain: 2,
    type: "single",
    stem: "Engineering wants an agentic IDE successor path for coding on AWS, not a staff knowledge bot. Which pairing is in the guide?",
    choices: [
      "Amazon Q Developer and Kiro",
      "Amazon Personalize and Amazon Forecast",
      "Amazon Textract and Amazon Translate only",
      "AWS Artifact and Amazon Macie only"
    ],
    answer: [0],
    explain: "Q Developer helps builders; Kiro is the newer agentic IDE direction. Q Business is for employees asking about company knowledge."
  },
  {
    id: "m3q17",
    domain: 2,
    type: "single",
    stem: "An airline hears that Bedrock does not use customer prompts to train the base provider models by default. Why does that matter?",
    choices: [
      "It is a favourite exam fact about data staying in your account/use path",
      "It means IAM is optional",
      "It means Guardrails are optional",
      "It means S3 is a vector database"
    ],
    answer: [0],
    explain: "AWS positions Bedrock so your prompts are not the providers' training set by default. You still own IAM, encryption, and content controls."
  },
  {
    id: "m3q18",
    domain: 2,
    type: "single",
    stem: "A startup serves unpredictable student traffic during enrollment week and wants to pay per request with no endpoints to patch. Which inference commercial model?",
    choices: [
      "Serverless / on-demand Bedrock-style inference",
      "A fleet of always-on self-managed GPU boxes they forgot to scale in",
      "Provisioned Throughput they never use at 3 a.m.",
      "Amazon Inspector assessment templates"
    ],
    answer: [0],
    explain: "Spiky unknown traffic fits serverless on-demand. Provisioned is for steady reserved capacity."
  },
  {
    id: "m3q19",
    domain: 2,
    type: "multi",
    stem: "Which TWO FM selection criteria should an insurer weigh when choosing a Bedrock model for claims chat?",
    choices: [
      "Modality, quality, latency, and token cost",
      "Context length, languages, and compliance needs",
      "The CEO's favourite font",
      "Whether Artifact has a SOC PDF (as the only criterion)",
      "The number of unused Elastic IPs"
    ],
    answer: [0, 1],
    explain: "The guide scores models on modality, quality, latency, cost, context, language, customisation, and compliance. Vanity and unused EIPs are not model scorecards."
  },
  {
    id: "m3q20",
    domain: 2,
    type: "multi",
    stem: "Which TWO statements about embeddings are true for a university search project?",
    choices: [
      "An embedding is a numeric vector that represents meaning",
      "Similar passages should sit near each other in vector space",
      "Embeddings replace the need for IAM",
      "Embeddings are the same as KMS customer master keys",
      "Embeddings are CloudTrail event IDs"
    ],
    answer: [0, 1],
    explain: "Embeddings enable semantic similarity search. They are not access control or encryption keys."
  },
  {
    id: "m3q21",
    domain: 2,
    type: "order",
    stem: "Order a typical foundation-model lifecycle from first to last (practitioner view).",
    items: [
      "Select data and a base model",
      "Optional customisation (prompt, RAG, or fine-tune)",
      "Evaluate quality and safety",
      "Deploy and collect feedback"
    ],
    answer: [0, 1, 2, 3],
    explain: "You almost never pre-train. You select, adapt lightly, evaluate, then deploy with a feedback loop."
  },
  {
    id: "m3q22",
    domain: 2,
    type: "match",
    stem: "Match each limitation of generative AI to a one-line meaning.",
    left: [
      "Fluent but wrong",
      "Same prompt, different answers",
      "Hard to say why the model chose a sentence"
    ],
    right: [
      "Nondeterminism",
      "Weak interpretability",
      "Hallucination",
      "Batch inference"
    ],
    answer: [2, 0, 1],
    explain: "Hallucinations are fluent errors. High temperature increases nondeterminism. FMs are weakly interpretable compared with small tabular models."
  },
  {
    id: "m3q23",
    domain: 3,
    type: "single",
    stem: "An airline legal bot must refuse to invent policy if the knowledge base has no hit. What instruction plus control pair is healthiest?",
    choices: [
      "Answer only from retrieved docs, say you do not know, and enable grounding checks",
      "Raise temperature so it improvises policy",
      "Pre-train a new FM nightly",
      "Store vectors only on CloudFront"
    ],
    answer: [0],
    explain: "Grounded refusals plus Guardrails grounding beat creative guessing when sources are missing."
  },
  {
    id: "m3q24",
    domain: 3,
    type: "single",
    stem: "Retrieved chunks are tiny sentence fragments, so answers miss the surrounding procedure. What chunking change is reasonable?",
    choices: [
      "Use larger windows, overlap, or hierarchical parent/child chunks",
      "Disable embeddings",
      "Switch the FM to Amazon Macie",
      "Delete the knowledge base"
    ],
    answer: [0],
    explain: "Too-small chunks lose context. Hierarchical or overlapping chunks keep section meaning without dumping the whole manual."
  },
  {
    id: "m3q25",
    domain: 3,
    type: "single",
    stem: "A university wants graph relationships among courses, prerequisites, and research papers in the RAG store. Which in-scope AWS database is the graph-shaped option?",
    choices: [
      "Amazon Neptune",
      "Amazon MemoryDB as the exam default",
      "Amazon CloudFront",
      "AWS Artifact"
    ],
    answer: [0],
    explain: "Neptune is the listed graph/vector-capable store. MemoryDB is out of scope. S3 and CloudFront are not vector databases."
  },
  {
    id: "m3q26",
    domain: 3,
    type: "single",
    stem: "Claims handlers need the model to return strict JSON with four keys and nothing else. Besides examples, which parameter helps halt extra prose?",
    choices: [
      "Stop sequences and a low max-token cap",
      "Amazon Personalize campaign",
      "Inspector rules packages",
      "Trusted Advisor service limits"
    ],
    answer: [0],
    explain: "Stop sequences and max tokens constrain length and format. Recommenders and vuln scanners do not stop generations."
  },
  {
    id: "m3q27",
    domain: 3,
    type: "single",
    stem: "Top-p is described to a new hire as 'another creativity knob'. What does nucleus sampling do?",
    choices: [
      "It samples from the smallest set of tokens whose probabilities sum to p",
      "It rotates KMS keys",
      "It trains a new FM",
      "It scans S3 for PII"
    ],
    answer: [0],
    explain: "Top-p (nucleus sampling) limits the token pool to a probability mass. Temperature and top-p both affect randomness."
  },
  {
    id: "m3q28",
    domain: 3,
    type: "single",
    stem: "An insurer wants reusable prompt templates with variables for product line and locale, stored like code. Which Bedrock feature?",
    choices: [
      "Amazon Bedrock Prompt Management",
      "Amazon Rekognition collections",
      "Amazon Forecast predictors",
      "AWS Snowball jobs"
    ],
    answer: [0],
    explain: "Prompt Management versions templates so product and locale variables stay consistent across releases."
  },
  {
    id: "m3q29",
    domain: 3,
    type: "single",
    stem: "The knowledge base is correct, but the model still answers the wrong product because the prompt never says which brand is in scope. What failed?",
    choices: [
      "Generation / prompt specification, not retrieval",
      "The OpenSearch index was empty",
      "Neptune had no vertices",
      "S3 versioning"
    ],
    answer: [0],
    explain: "If docs are right and the answer is still wrong, fix the prompt, model, or temperature — a generation failure."
  },
  {
    id: "m3q30",
    domain: 3,
    type: "single",
    stem: "A startup wants a cheaper student model that mimics a large teacher used for complex underwriting narratives. Which customisation?",
    choices: [
      "Distillation",
      "Amazon Textract AnalyzeID only",
      "AWS Artifact",
      "Amazon Macie"
    ],
    answer: [0],
    explain: "Distillation copies teacher behaviour into a smaller, cheaper student. It is not OCR or a compliance PDF."
  },
  {
    id: "m3q31",
    domain: 3,
    type: "single",
    stem: "Faculty compare a model translation of a syllabus against a professional reference translation. Which overlap metric is the usual pick?",
    choices: [
      "BLEU",
      "Recall of a fraud model",
      "Amazon Inspector severity",
      "Trusted Advisor idle-load-balancer checks"
    ],
    answer: [0],
    explain: "BLEU is the classic translation overlap metric. ROUGE is the usual summary overlap metric."
  },
  {
    id: "m3q32",
    domain: 3,
    type: "single",
    stem: "An airline wants Bedrock to run automatic quality and toxicity comparisons between two models before go-live. Which capability?",
    choices: [
      "Amazon Bedrock Model Evaluation",
      "Amazon Personalize recipes",
      "Amazon Polly lexemes",
      "AWS Transform waves"
    ],
    answer: [0],
    explain: "Bedrock Model Evaluation compares models on quality and safety-style dimensions. It is not a recommender or TTS feature."
  },
  {
    id: "m3q33",
    domain: 3,
    type: "multi",
    stem: "Which TWO prompt techniques should a claims team try before any training job?",
    choices: [
      "Zero-shot instructions that state the task and format",
      "Few-shot examples of good claim summaries",
      "Pre-training a new FM on the public web",
      "Amazon Forecast seasonality",
      "Inspector CVE suppression"
    ],
    answer: [0, 1],
    explain: "Start with instructions and a few examples. Pre-training a new FM is almost never the practitioner move."
  },
  {
    id: "m3q34",
    domain: 3,
    type: "multi",
    stem: "A university RAG bot cites the wrong syllabus because search returned last year's course. Which TWO retrieval fixes apply?",
    choices: [
      "Metadata filters on academic year",
      "Re-rank or hybrid search so the current syllabus ranks first",
      "Raise temperature so it invents this year's dates",
      "Disable embeddings and paste the entire catalogue every call",
      "Turn off IAM"
    ],
    answer: [0, 1],
    explain: "Wrong document is a retrieval failure. Filters and better search fix it. Higher temperature makes generation worse."
  },
  {
    id: "m3q35",
    domain: 3,
    type: "order",
    stem: "Put these customisation paths from lowest typical spend to highest.",
    items: [
      "Prompt / in-context learning",
      "RAG",
      "Fine-tuning",
      "Pre-train from scratch"
    ],
    answer: [0, 1, 2, 3],
    explain: "Same cost ladder as the exam: prompt → RAG → fine-tune → almost never pre-train."
  },
  {
    id: "m3q36",
    domain: 3,
    type: "match",
    stem: "Match each customisation to when you use it.",
    left: [
      "Facts that change every week",
      "Stable tone on labeled pairs",
      "Cut latency by copying a teacher"
    ],
    right: [
      "Fine-tuning",
      "Distillation",
      "RAG",
      "Amazon Polly"
    ],
    answer: [2, 0, 1],
    explain: "Changing facts → RAG. Style with labels → fine-tune. Cheaper student → distillation."
  },
  {
    id: "m3q37",
    domain: 4,
    type: "single",
    stem: "An airline chatbot must block violent or hateful completions even if a passenger goads the model. Which Guardrails family?",
    choices: [
      "Content filters",
      "Amazon Forecast predictors",
      "SageMaker JumpStart kernels",
      "AWS Snowmobile"
    ],
    answer: [0],
    explain: "Content filters target hate, violence, and sexual content at runtime. They are harder than a prompt that says 'be nice'."
  },
  {
    id: "m3q38",
    domain: 4,
    type: "single",
    stem: "Underwriters want to see which tabular features drove a decline before they send the letter. Which SageMaker tool?",
    choices: [
      "SageMaker Clarify",
      "Amazon Lex sample utterances",
      "Amazon Translate",
      "Amazon Personalize"
    ],
    answer: [0],
    explain: "Clarify provides bias metrics and feature attribution for explainability."
  },
  {
    id: "m3q39",
    domain: 4,
    type: "single",
    stem: "A university publishes intended use, metrics, and known limits of its admissions model for an ethics board. Which artifact?",
    choices: [
      "SageMaker Model Cards",
      "Amazon Polly SSML",
      "CloudFront cache behaviours",
      "An Inspector suppression rule"
    ],
    answer: [0],
    explain: "Model Cards document intended use and limitations. They support transparency reviews."
  },
  {
    id: "m3q40",
    domain: 4,
    type: "single",
    stem: "After a holiday schedule change, an airline no-show model still looks accurate on last month's holdout but fails in production. What should they turn on?",
    choices: [
      "SageMaker Model Monitor",
      "Amazon Textract queries",
      "AWS Artifact reports as the only fix",
      "Higher top-p"
    ],
    answer: [0],
    explain: "Production drift is Model Monitor's job. A SOC PDF does not detect feature drift."
  },
  {
    id: "m3q41",
    domain: 4,
    type: "single",
    stem: "A claims model is highly accurate but nobody can explain a single decision. Counsel says interpretability is mandatory. What tradeoff is this?",
    choices: [
      "The most accurate model may be the least explainable; consider a simpler model plus Clarify",
      "Raise temperature to add explanations",
      "Disable logging to become transparent",
      "Use Amazon Polly to speak the score"
    ],
    answer: [0],
    explain: "Accuracy versus interpretability is a responsible-AI tradeoff. FMs and deep nets often lose the 'why' argument."
  },
  {
    id: "m3q42",
    domain: 4,
    type: "multi",
    stem: "Which TWO human-centred design habits should an insurer add around a denial chatbot?",
    choices: [
      "Show sources or a rationale when possible and collect user feedback",
      "Keep a human reviewer for high-stakes denials (A2I)",
      "Hide every uncertainty so customers never question the bot",
      "Set temperature to maximum",
      "Turn off CloudTrail"
    ],
    answer: [0, 1],
    explain: "Responsible design shows why, accepts feedback, and keeps humans on high-stakes paths."
  },
  {
    id: "m3q43",
    domain: 4,
    type: "multi",
    stem: "Which TWO Guardrails configurations stop a university bot from discussing banned exam-cheating tactics and from leaking emails?",
    choices: [
      "Denied topics",
      "PII filters",
      "Amazon Personalize recipes",
      "AWS Transform waves",
      "CloudFront price class All"
    ],
    answer: [0, 1],
    explain: "Denied topics block whole subjects. PII filters redact emails and similar identifiers."
  },
  {
    id: "m3q44",
    domain: 5,
    type: "single",
    stem: "Only the actuarial role should invoke a costly Bedrock model ID. Which control enforces that?",
    choices: [
      "IAM policies (and condition keys on model IDs)",
      "A system prompt that says 'actuaries only'",
      "Higher temperature",
      "Amazon Polly"
    ],
    answer: [0],
    explain: "Who can call which model is IAM. A prompt cannot enforce identity."
  },
  {
    id: "m3q45",
    domain: 5,
    type: "single",
    stem: "API keys for a rating bureau sit in the agent prompt. Where should those secrets move?",
    choices: [
      "AWS Secrets Manager (and AgentCore identity for the call)",
      "The few-shot examples file in Slack",
      "A public GitHub gist",
      "The temperature field"
    ],
    answer: [0],
    explain: "Secrets never belong in prompts. Secrets Manager plus least-privilege tool identity is the pattern."
  },
  {
    id: "m3q46",
    domain: 5,
    type: "single",
    stem: "An airline must show that S3 training buckets containing passport images are being inventoried for sensitive data. Which service?",
    choices: [
      "Amazon Macie",
      "Amazon Lex",
      "Amazon Personalize",
      "Amazon Forecast"
    ],
    answer: [0],
    explain: "Macie discovers sensitive data in S3. Guardrails filter live model I/O; they do not inventory forgotten buckets."
  },
  {
    id: "m3q47",
    domain: 5,
    type: "single",
    stem: "Security wants Bedrock reachable only from the claims VPC. Which networking pattern?",
    choices: [
      "AWS PrivateLink / interface VPC endpoint",
      "A public 0.0.0.0/0 security group 'for convenience'",
      "Raising top-p",
      "Amazon Translate custom terminology"
    ],
    answer: [0],
    explain: "PrivateLink keeps traffic on the AWS network and off the public internet."
  },
  {
    id: "m3q48",
    domain: 5,
    type: "single",
    stem: "Internal audit wants a managed way to collect evidence that encryption and logging controls still operate, not a one-time PDF download. Which service?",
    choices: [
      "AWS Audit Manager",
      "Amazon Rekognition",
      "Amazon Polly",
      "Amazon Personalize"
    ],
    answer: [0],
    explain: "Audit Manager continuously gathers evidence. Artifact is where you download AWS's own reports."
  },
  {
    id: "m3q49",
    domain: 5,
    type: "single",
    stem: "A university must keep student prompts inside an approved Region. What governance topic is this?",
    choices: [
      "Data residency",
      "ROUGE optimisation",
      "Top-p tuning",
      "JumpStart kernel choice only"
    ],
    answer: [0],
    explain: "Residency limits where data is processed and stored. Cross-Region inference needs an explicit policy decision."
  },
  {
    id: "m3q50",
    domain: 5,
    type: "multi",
    stem: "Which TWO AWS services help an airline watch Bedrock API activity and resource configuration drift around the knowledge base?",
    choices: [
      "AWS CloudTrail for API who/when",
      "AWS Config for configuration history",
      "Amazon Polly lexicons",
      "Amazon Personalize filters",
      "Raising temperature"
    ],
    answer: [0, 1],
    explain: "CloudTrail is the API audit trail. Config records how resources change. TTS and recommenders are not governance planes."
  }
];
