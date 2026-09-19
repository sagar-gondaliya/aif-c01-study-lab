from common import meaning, exam, trap, h2, p, ul, table, q_single, q_multi, q_order, q_match, topic


def topics():
    return [
        topic(
            "d4-features",
            4,
            "4.1",
            "Features of responsible AI and sustainability",
            "Task 4.1 starts with the word list. Learn it like Domain 1 terms.",
            meaning(
                "Task 4.1 starts with these words. Learn them the same way you learned accuracy and precision.",
                [
                    "<b>Bias</b> — a repeated error that helps or hurts a group. <b>Fairness</b> — similar outcomes for similar people.",
                    "<b>Inclusivity</b> — the data and the product cover many users, not one group. <b>Robustness</b> — it still works on messy or attacking input.",
                    "<b>Safety</b> — it avoids harm. <b>Veracity</b> — the answer is true. Veracity is <b>not</b> encryption.",
                    "<b>Sustainability</b> — a large model and a long prompt use more energy. Prefer a smaller model, caching, or batch when that is enough.",
                ],
                "1. A résumé screener scores one group much worse with no job-related reason → <b>fairness / bias</b>.<br>"
                "2. A 24/7 FAQ bot uses Nova Micro (small cheap model) instead of the largest model → cost, speed, and <b>sustainability</b>.<br>"
                "3. A bot states a false IAM action as fact → <b>veracity</b> failed (not a KMS problem).",
            )
            + exam(
                "They give a story (“the loan model rejects one postcode”) and ask which principle is broken (fairness/bias). "
                "They ask why a team picked Nova Micro for FAQ (cost + sustainability + latency)."
            )
            + trap(
                "Veracity is not the same as encryption. Robustness is not the same as IAM. Sustainability is not “turn off CloudTrail.”"
            ),
            [
                q_single(
                    "A hiring model scores one demographic group much worse with no job-related reason. Which principle is at risk?",
                    ["Fairness (and bias)", "Token caching", "Glacier vaults", "Prompt Management versions"],
                    0,
                    "Unequal outcomes = fairness/bias.",
                ),
                q_single(
                    "A bot states false medical doses confidently. Which responsible-AI feature failed?",
                    ["Veracity (truthfulness)", "CloudFront caching", "Budgets alerts", "ECS task CPU"],
                    0,
                    "Truthfulness = veracity.",
                ),
                q_single(
                    "The model still works when users typo and try mild jailbreaks. Which feature is that closer to?",
                    ["Robustness", "Amazon Personalize", "Redshift vacuum", "HealthScribe"],
                    0,
                    "Holds up under messy/adversarial input = robustness.",
                ),
                q_single(
                    "Leadership asks to shrink energy use of a 24/7 FAQ bot. Which responsible choice?",
                    [
                        "Smaller model, shorter context, caching/batch — do not pre-train a new FM",
                        "Always use the largest premier model",
                        "Paste the data lake into every prompt",
                        "Disable all evaluation",
                    ],
                    0,
                    "Sustainability tracks the customisation/cost ladder.",
                ),
                q_multi(
                    "Which TWO are named responsible-AI features?",
                    [
                        "Inclusivity",
                        "Safety",
                        "Instance tenancy of EC2",
                        "S3 storage class algorithm",
                        "CloudFront price class",
                    ],
                    [0, 1],
                    "Bias, fairness, inclusivity, robustness, safety, veracity.",
                ),
                q_match(
                    "Match the word.",
                    ["Bias", "Fairness", "Veracity", "Sustainability"],
                    ["Comparable outcomes across groups", "Systematic error that favours or harms", "Energy / environmental cost of large models", "Truthfulness of outputs"],
                    [1, 0, 3, 2],
                    "Bias / fairness / veracity / sustainability.",
                ),
            ],
        ),
        topic(
            "d4-legal",
            4,
            "4.1",
            "Legal risks and dataset quality",
            "GenAI creates new legal and trust problems. Datasets must not be a dirty grab-bag.",
            meaning(
                "GenAI can create legal and trust problems. Training files must not be a random dump.",
                [
                    "Name the risks: <b>IP / copyright</b> (copying someone else’s work), biased answers, lost trust, harm to a user, invented facts treated as true, personal data leaks.",
                    "Datasets should be inclusive, diverse, cleaned, balanced, and used with permission.",
                    "Open-source model files help people inspect the model. They do <b>not</b> automatically remove bias or copyright risk.",
                ],
                "1. A generator copies a copyrighted vendor manual almost word-for-word → <b>IP risk</b>.<br>"
                "2. A face dataset is almost only one age and skin tone → not diverse / balanced.<br>"
                "3. A chatbot invents a refund rule and a customer acts on it → <b>hallucination + harm</b>.",
            )
            + exam(
                "“Marketing used a model that copies a living artist’s style and a lawsuit arrives” = IP risk. "
                "“Training set is 95% one city” = not diverse/balanced. "
                "They will not ask you to write a contract. They ask you to name the risk."
            )
            + trap(
                "Open-source weights can improve transparency but can also raise safety/IP tradeoffs — do not treat “open” as automatically responsible."
            ),
            [
                q_single(
                    "A generator outputs a paragraph that closely copies a copyrighted guidebook. Primary risk type?",
                    ["Intellectual property / copyright", "S3 inventory only", "ECS placement", "Trusted Advisor idle RDS"],
                    0,
                    "Copied expression = IP risk.",
                ),
                q_single(
                    "A chatbot invents a refund policy and a customer relies on it. Which pair of issues?",
                    ["Hallucination + end-user harm / trust", "Only Glacier restore", "Only JumpStart stars", "Only EMR bootstrap"],
                    0,
                    "False fluent text that people act on.",
                ),
                q_single(
                    "A face dataset is almost only one age and skin tone. What dataset quality is missing?",
                    ["Diversity / inclusivity / balance", "Provisioned Throughput", "Prompt caching", "Nova Reel fps"],
                    0,
                    "Skewed data → skewed model.",
                ),
                q_single(
                    "Which dataset practice matches the guide?",
                    [
                        "Curate and balance sources; know your rights to use the data",
                        "Scrape everything including secrets and hope",
                        "Use only one duplicated record",
                        "Never document intended use",
                    ],
                    0,
                    "Inclusive, diverse, curated, balanced.",
                ),
                q_multi(
                    "Which TWO are GenAI legal/business risks they expect?",
                    [
                        "IP claims on outputs or training data",
                        "Loss of trust from biased or false answers",
                        "CloudFront price class 200",
                        "The colour of the SageMaker notebook theme",
                        "Whether Lambda has 128 MB or 256 MB for a hello-world",
                    ],
                    [0, 1],
                    "IP, bias, trust, harm, hallucinations-as-fact.",
                ),
                q_single(
                    "Why is “we used an open-source FM” not a complete responsible-AI answer?",
                    [
                        "Licenses, safety, and data provenance still need review",
                        "Open-source models are illegal on AWS",
                        "Open-source models cannot run on Bedrock or JumpStart",
                        "Open-source always removes bias",
                    ],
                    0,
                    "Transparency vs safety/IP is a tradeoff they mention.",
                ),
            ],
        ),
        topic(
            "d4-guard",
            4,
            "4.1",
            "Amazon Bedrock Guardrails (the lock)",
            "If the stem says ensure / prevent / must not — this is usually the answer.",
            meaning(
                "If the question says <i>ensure / prevent / must not</i>, pick <b>Guardrails</b> (a filter that runs on every call). A polite sentence in the prompt is only a request.",
                [
                    "Guardrails check what goes <b>in</b> and what comes <b>out</b> of the model.",
                    "Types: content filters (hate, sexual, violence), denied topics, blocked words, PII filters (hide personal data), grounding (stay on the sources), help against prompt attacks.",
                    "Guardrails = <b>what text</b> is allowed. <b>IAM</b> = <b>which person or role</b> may call the model.",
                    "<b>Macie</b> finds personal data already sitting in S3. <b>Comprehend</b> finds personal data in text you send it. Guardrails filter the live chat.",
                ],
                "1. A bank must block investment advice, not only ask the model to refuse → Guardrails <b>denied topics</b>.<br>"
                "2. Answers must never include national IDs → Guardrails <b>PII filter</b>.<br>"
                "3. IAM already limits who can call Claude, but users still trick it into medical dosing → add Guardrails. IAM is not a content filter.",
            )
            + exam(
                "“Must not give legal advice” = denied topic (plus maybe A2I), not “please don’t.” "
                "“Must not echo SSNs” = PII filter. "
                "“Must not answer off the KB” = grounding. "
                "Hate/sexual/violence = content filters."
            )
            + trap(
                "Guardrails ≠ IAM. Guardrails = <b>what content</b> is allowed. IAM = <b>who</b> can call the model. "
                "Comprehend finds PII in text you send it. Macie finds PII sitting in S3. Guardrails filter <b>model I/O</b>."
            ),
            [
                q_single(
                    "A bank must block the bot from giving investment advice, not merely ask it to refuse. What do they configure?",
                    ["Bedrock Guardrails denied topics", "A higher temperature", "Amazon Forecast", "S3 Glacier"],
                    0,
                    "Ensure/prevent a topic = Guardrails.",
                ),
                q_single(
                    "Outputs must never include national IDs. Which Guardrails family?",
                    ["PII / sensitive-information filters", "Amazon Personalize", "JumpStart", "AWS Transform"],
                    0,
                    "PII out of the model = Guardrails PII.",
                ),
                q_single(
                    "They need to block hate and graphic violence in both prompts and completions. Which control?",
                    ["Guardrails content filters", "Amazon Translate", "Amazon Polly", "AWS Data Exchange"],
                    0,
                    "Hate/violence = content filters.",
                ),
                q_single(
                    "IAM already limits who can invoke Claude. Users still trick it into medical dosing. What is missing?",
                    ["Guardrails (content / topics) — IAM is not a content filter", "More IAM users", "Disable KMS", "Delete the KB"],
                    0,
                    "Who vs what.",
                ),
                q_multi(
                    "Which TWO statements are correct?",
                    [
                        "A prompt instruction is a soft request; Guardrails are a hard control",
                        "Guardrails can check grounding against sources",
                        "Guardrails replace KMS encryption keys",
                        "Guardrails are only available on Amazon Forecast",
                        "Guardrails delete CloudTrail",
                    ],
                    [0, 1],
                    "Hard content control + grounding. Not encryption.",
                ),
                q_match(
                    "Match the filter to the stem.",
                    ["Denied topics", "PII filter", "Content filters", "Contextual grounding"],
                    ["No SSNs in the reply", "Answer must stick to retrieved docs", "No legal advice", "No hate / sexual / violence"],
                    [2, 0, 3, 1],
                    "Topic / PII / harm categories / grounding.",
                ),
            ],
        ),
        topic(
            "d4-tools",
            4,
            "4.1",
            "Clarify, Model Monitor, Model Cards, A2I, toxicity",
            "Each responsible-AI tool has one job. Do not mix them.",
            meaning(
                "Each responsible-AI tool has one job. Do not mix them.",
                [
                    "<b>SageMaker Clarify</b> — finds bias and shows which columns pushed a prediction.",
                    "<b>SageMaker Model Monitor</b> — watches live quality. Alerts if the data or accuracy changes (drift).",
                    "<b>Model Cards / AI Service Cards</b> — a short document: intended use, data, known limits.",
                    "<b>Bedrock Model Evaluation</b> — compare two models on quality or toxicity.",
                    "<b>A2I</b> — a person reviews a low-confidence or high-risk answer before it is sent.",
                    "High bias (underfit) = wrong for everyone. High variance (overfit) = fails on new data. Demographic bias = unfair for a group.",
                ],
                "1. A credit model must show which columns pushed a decline → <b>Clarify</b>.<br>"
                "2. Precision fell after a new product launch → <b>Model Monitor</b>.<br>"
                "3. A clinician must approve a low-confidence extraction → <b>A2I</b>.<br>"
                "4. “Which foundation model is less toxic?” → <b>Bedrock Model Evaluation</b>.",
            )
            + table(
                ["Tool", "Job"],
                [
                    ["SageMaker Clarify", "Bias detection + feature attribution / explainability"],
                    ["SageMaker Model Monitor", "Drift and quality in production"],
                    ["SageMaker Model Cards", "Document intended use, metrics, limits, data"],
                    ["AI Service Cards", "AWS’s own transparency docs for AI services"],
                    ["Bedrock Model Evaluation", "Compare models on quality / toxicity"],
                    ["Amazon A2I", "Human review of low-confidence or high-risk outputs"],
                    ["Bedrock Guardrails", "Runtime content / PII / topics / grounding"],
                ],
            )
            + h2("Bias vs variance (they mix Domain 1)")
            + ul(
                [
                    "Demographic bias → unfair outcomes",
                    "High bias (underfit) → inaccurate for everyone",
                    "High variance (overfit) → brittle on new data",
                ]
            )
            + exam(
                "“Which features drove the score?” = Clarify. "
                "“Accuracy dropped after a holiday” = Model Monitor. "
                "“Document intended use for auditors” = Model Cards. "
                "“A human must approve the refund letter” = A2I. "
                "“Which FM is less toxic?” = Bedrock evaluation."
            )
            + trap(
                "Clarify does not filter live chat (that is Guardrails). Model Cards do not encrypt data (that is KMS)."
            ),
            [
                q_single(
                    "A credit model must show which inputs pushed a decline. Which tool?",
                    ["SageMaker Clarify", "Amazon Polly", "Amazon Lex", "AWS Transform"],
                    0,
                    "Explainability / bias = Clarify.",
                ),
                q_single(
                    "Live traffic drifted after a product launch and precision fell. Which tool?",
                    ["SageMaker Model Monitor", "Amazon Rekognition", "Amazon Translate", "Amazon Personalize"],
                    0,
                    "Production drift = Model Monitor.",
                ),
                q_single(
                    "Auditors want a one-pager: intended use, data, metrics, limits. Which artifact?",
                    ["SageMaker Model Cards (or AI Service Cards for AWS services)", "Amazon Forecast predictor only", "A Glacier inventory", "An EMR step"],
                    0,
                    "Documentation = Model Cards.",
                ),
                q_single(
                    "Low-confidence medical extraction must be seen by a clinician. Which service?",
                    ["Amazon A2I", "Amazon Macie only", "AWS Budgets", "Amazon CloudFront"],
                    0,
                    "Human review = A2I.",
                ),
                q_multi(
                    "Which TWO map correctly?",
                    [
                        "Toxicity comparison of two Bedrock models → Model Evaluation",
                        "Runtime hate filter → Guardrails",
                        "Runtime hate filter → Clarify feature store",
                        "Drift → Prompt Management only",
                        "Feature reasons → Amazon Transcribe",
                    ],
                    [0, 1],
                    "Eval for toxicity; Guardrails for live filters.",
                ),
                q_match(
                    "Match the tool.",
                    ["Clarify", "Model Monitor", "Model Cards", "A2I"],
                    ["Drift in production", "Human review", "Bias / feature attribution", "Intended-use documentation"],
                    [2, 0, 3, 1],
                    "Clarify / Monitor / Cards / A2I.",
                ),
            ],
        ),
        topic(
            "d4-xai",
            4,
            "4.2",
            "Transparent versus explainable",
            "Task 4.2 is this distinction. FMs are often less explainable than a tree.",
            meaning(
                "On this exam, <b>transparent</b> and <b>explainable</b> are two different words. Do not treat them as the same.",
                [
                    "<b>Transparent</b> — you can inspect how it was built: data sources, design, Model Card, limits, intended use.",
                    "<b>Explainable</b> — you can say why <i>this one</i> prediction happened (Clarify, which columns mattered, a simple tree or linear model).",
                    "A foundation model can have a Model Card and still not explain one token it wrote.",
                    "The most accurate model may be the hardest to explain. If a regulator needs reasons for each decision → classic ML + Clarify, not Claude.",
                ],
                "1. You publish data sources and known limits for a fraud model → <b>transparency</b> (Model Card).<br>"
                "2. A regulator asks why <i>this</i> application scored 0.91 → <b>explainability</b> (Clarify).<br>"
                "3. CloudTrail tells you who called the API → that is <b>audit</b>, not “which column caused the score.”",
            )
            + exam(
                "“Publish a card of limits and data” = transparency. "
                "“Why was THIS application denied?” = explainability. "
                "They will offer Claude as the explainability answer — that is usually wrong."
            )
            + trap(
                "Logging (CloudTrail) is audit, not feature attribution. Open weights help transparency; they do not automatically explain one prediction."
            ),
            [
                q_single(
                    "A team publishes data sources, intended use, and known limits for a model. Which idea?",
                    ["Transparency", "Top-p sampling", "Prompt injection", "Batch inference"],
                    0,
                    "Cards and docs = transparency.",
                ),
                q_single(
                    "A regulator asks why THIS applicant was declined. Which idea?",
                    ["Explainability (feature-level reasons)", "Only a larger FM", "Higher temperature", "Amazon Polly"],
                    0,
                    "Why this score = explainable.",
                ),
                q_single(
                    "Why might a linear model beat Claude for credit decisions on this exam?",
                    [
                        "It is more explainable even if an FM is flashier",
                        "Claude cannot run on AWS",
                        "Linear models always have better ROUGE",
                        "FMs are illegal in finance forever",
                    ],
                    0,
                    "Interpretability tradeoff.",
                ),
                q_single(
                    "Which AWS tool is the usual explainability pick?",
                    ["SageMaker Clarify", "Amazon Q Developer", "Amazon Kendra only", "AWS Transform"],
                    0,
                    "Clarify = attribution / bias.",
                ),
                q_multi(
                    "Which TWO statements are true?",
                    [
                        "FMs are often less explainable than trees or linear models",
                        "Transparency and explainability are the same word",
                        "The most accurate model may be the least interpretable",
                        "Model Cards compute SHAP values automatically for every token",
                        "Explainability is only a Domain 2 token price",
                    ],
                    [0, 2],
                    "They are different; accuracy vs interpretability is a tradeoff.",
                ),
                q_match(
                    "Match the request.",
                    ["Show the Model Card", "Show why this row scored 0.91", "Compare toxicity of two FMs", "Filter hate at runtime"],
                    ["Clarify / feature attribution", "Guardrails", "Transparency documentation", "Bedrock Model Evaluation"],
                    [2, 0, 3, 1],
                    "Card / why / eval / filter.",
                ),
            ],
        ),
        topic(
            "d4-hcd",
            4,
            "4.2",
            "Human-centred design for AI",
            "People stay in the loop for high stakes. The UI should show limits.",
            meaning(
                "For high-stakes answers, a person stays in the loop. The screen must not hide that a model wrote the text.",
                [
                    "Show a source (citation) or a label that the reply is AI-generated. Give a “this was wrong” button.",
                    "Keep a human for high-risk output (<b>A2I</b>). Users must be able to override.",
                    "Do not stamp a guess as “official policy” or “verified legal advice.”",
                    "Inclusivity is also the product: readable screens, more than one language, test with many kinds of users.",
                ],
                "1. A benefits bot shows the source paragraph under each answer and a report button → <b>human-centred</b>.<br>"
                "2. Loan decline letters need a specialist before send → <b>A2I</b>.<br>"
                "3. The UI stamps every chatbot reply “verified legal advice” → irresponsible. It hides that the text is a guess.",
            )
            + exam(
                "“Show citations under each answer” = human-centred + grounding. "
                "“Clinician confirms before send” = A2I / human-centred. "
                "“No way to report a bad answer” = missing feedback."
            )
            + trap(
                "Human-centred is not “remove all logs.” It is not “the model is always right.”"
            ),
            [
                q_single(
                    "A benefits bot must show the source paragraph under each answer and a “this was wrong” button. What design idea is that?",
                    ["Human-centred (transparency + feedback)", "Maximum temperature", "Disable Guardrails", "Hide all citations"],
                    0,
                    "Citations + feedback = human-centred.",
                ),
                q_single(
                    "Loan declines must be reviewable by a specialist before the letter goes out. Which AWS name?",
                    ["Amazon A2I", "Amazon Forecast", "Amazon Personalize", "Amazon Rekognition"],
                    0,
                    "Human review = A2I.",
                ),
                q_single(
                    "The UI labels every chatbot reply as “verified legal advice.” Why is that irresponsible?",
                    [
                        "It hides uncertainty and can cause harm if the model is wrong",
                        "Labels are illegal on AWS",
                        "FMs cannot generate text",
                        "Citations are forbidden",
                    ],
                    0,
                    "Do not over-claim certainty.",
                ),
                q_single(
                    "Which practice supports inclusivity in the product, not only the dataset?",
                    [
                        "Accessible UI, multiple languages, and testing with diverse users",
                        "Training only on one dialect and one device",
                        "Removing keyboard access",
                        "English-only error codes for a global audience with no alternative",
                    ],
                    0,
                    "Inclusivity is also the experience.",
                ),
                q_multi(
                    "Which TWO belong in human-centred AI on this exam?",
                    [
                        "A path for humans to override high-stakes outputs",
                        "A way to collect user feedback",
                        "Forbidding any documentation of limits",
                        "Presenting guesses as statutory truth",
                        "Removing IAM so “anyone can help”",
                    ],
                    [0, 1],
                    "Override + feedback. Not fake certainty or open IAM.",
                ),
                q_single(
                    "Why keep a human in the loop for medical or legal generation?",
                    [
                        "High harm if the model is wrong; A2I / specialist review",
                        "Humans raise BLEU automatically",
                        "Bedrock cannot log anything",
                        "Guardrails are illegal in those industries",
                    ],
                    0,
                    "Stakes × error cost = human review.",
                ),
            ],
        ),
    ]
