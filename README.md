# Travel Reimbursement Approval Agent

## 1. Project Title
Travel Reimbursement Approval Agent – Agentic AI-Based Expense Validation and Approval System.

## 2. Brief One Line Summary
An AI-powered reimbursement approval system that automates employee travel expense validation using policy-based checks, intelligent tool orchestration, and human-in-the-loop review.

## 3. Overview
The Travel Reimbursement Approval Agent is designed to automate the initial review of employee travel reimbursement claims.

The system evaluates expense claims against company policies, checks supporting receipts, validates expense limits, identifies duplicate transactions, and determines the appropriate approval status.

It uses a Python-based agent orchestration workflow with deterministic business rules and optional LLM-based tool selection.

## 4. Problem Statement
Manual travel reimbursement processing involves several time-consuming activities:

- Checking expense eligibility against company policies.
- Validating receipts and supporting documents.
- Verifying meal, lodging, and transportation limits.
- Identifying duplicate expenses.
- Checking submission deadlines.
- Routing exceptional claims for manual approval.

The objective is to automate these activities, improve consistency, reduce manual effort, and provide transparent reimbursement decisions.

## 5. Dataset
The project uses five sample employee reimbursement claims provided in the assignment.

| Claim ID | Scenario |
|---|---|
| CLM-001 | Industry conference travel |
| CLM-002 | Weekend hotel stay |
| CLM-003 | Client site visit |
| CLM-004 | International vendor negotiation |
| CLM-005 | Client dinner / business development |

The dataset contains employee information, business purpose, travel dates, expense categories, claimed amounts, and receipt availability.

A Python-based policy knowledge base stores the reimbursement rules and policy references.

## 6. Tools and Technologies
- Python
- Jupyter Notebook
- OpenAI Function Calling (optional)
- Pandas
- Matplotlib
- JSON
- Rule-Based Decision Engine
- Agent Orchestration
- IPython

## 7. Methods
The project follows an agentic workflow:

1. Claim Intake – Accept employee reimbursement claims.
2. Policy Lookup – Retrieve relevant company reimbursement policies.
3. Receipt Validation – Check mandatory supporting documents.
4. Expense Validation – Verify eligible categories and reimbursement limits.
5. Timeliness Validation – Check the 30-day submission policy.
6. Duplicate Detection – Identify repeated expense items.
7. Approval Threshold Validation – Determine the applicable approval tier.
8. Decision Engine – Generate the final reimbursement decision.
9. Output Validation – Validate the structured JSON response.
10. Audit and Reporting – Maintain tool execution results and generate a dashboard.

The system supports four decisions:

- APPROVE
- PARTIAL_APPROVE
- REJECT
- MANUAL_REVIEW

## 8. Key Insights
- Automatically identifies eligible and ineligible expenses.
- Detects missing mandatory receipts.
- Calculates reimbursement amounts based on policy limits.
- Identifies potential duplicate expense items.
- Routes exceptional and high-value claims for manual review.
- Maintains policy references for auditability.
- Generates consistent structured JSON responses.

## 9. Dashboard/Model/Output
The project generates:

- Claim-wise reimbursement decision summary.
- Approved and deducted amount calculations.
- Missing document identification.
- Policy reference tracking.
- Agent tool execution audit trail.
- Dashboard showing decision distribution and financial summaries.
- Structured JSON output containing nine required fields.

The output includes claim ID, decision, approved amount, deducted amount, missing documents, policy references, confidence, explanation, and tools used.

## 10. How to Run this project?

### Step 1: Install Python dependencies

```bash
pip install notebook pandas matplotlib ipython
```

### Step 2: Start Jupyter Notebook

```bash
jupyter notebook
```

### Step 3: Open the project

Open:

`Travel_Reimbursement_Approval_Agent.ipynb`

### Step 4: Execute the notebook

Select:

**Kernel → Restart & Run All**

Alternatively, upload the notebook to Google Colab and select:

**Runtime → Run all**

### Step 5: View the results

The notebook will execute the complete workflow and display:

- Reimbursement decisions.
- Policy validation results.
- Agent execution logs.
- Dashboard visualizations.
- Final structured JSON output.

### Optional: Enable OpenAI Function Calling

Install the OpenAI SDK:

```bash
pip install openai
```

Configure your `OPENAI_API_KEY` environment variable before starting Jupyter.

Without an API key, the project automatically uses its local rule-based tool planner.

---

**Project Status:** Working Python-based Agentic AI prototype.

**Future Enhancements:** LangGraph orchestration, Azure AI Document Intelligence, persistent audit storage, historical duplicate detection, and human-in-the-loop approval integration.
## 11. Results & Conclusion

### Results
The Travel Reimbursement Approval Agent successfully evaluates all five sample reimbursement claims using automated policy validation and agent-based tool orchestration.

The system demonstrates the following outcomes:

- **CLM-001:** APPROVE – All expenses comply with reimbursement policies.
- **CLM-002:** REJECT – Contains ineligible spa and minibar expenses.
- **CLM-003:** PARTIAL_APPROVE – Lodging expense exceeds the permitted limit.
- **CLM-004:** MANUAL_REVIEW – Business-class airfare, missing receipt, and high-value claim.
- **CLM-005:** MANUAL_REVIEW – Required meal receipt is missing.

### Conclusion
The project demonstrates how Agentic AI and Python-based automation can simplify employee travel reimbursement processing.

By combining policy lookup, multiple validation tools, deterministic decision-making, structured JSON output, and human-in-the-loop review, the solution provides a transparent and auditable reimbursement workflow.

It also demonstrates the practical application of AI agents in enterprise business process automation.

## 12. Future Work

The following enhancements can extend the current prototype:

- **LangGraph Integration:** Implement stateful agent orchestration, conditional routing, and workflow management.
- **Azure OpenAI Integration:** Enable intelligent LLM-based reasoning and tool selection.
- **Document Intelligence:** Integrate Azure AI Document Intelligence for automatic receipt extraction.
- **RAG Integration:** Retrieve reimbursement policies using vector search and semantic retrieval.
- **Human-in-the-Loop:** Implement manager approval and exception-handling workflows.
- **Database Integration:** Store employee claims, reimbursement history, and audit records.
- **Production Deployment:** Deploy the application using FastAPI and Azure cloud services.
- **Monitoring & Evaluation:** Add execution tracking, logging, performance monitoring, and evaluation metrics.

## 13. Author & Contact

**Author:** Krishna Kumar

**Project:** Travel Reimbursement Approval Agent

**Technical Focus:** Python | Generative AI | Agentic AI | LLMs | Automation

**Email:** kknup2609@gmail.com

**Location:** Pune, India

**GitHub:** Add your GitHub profile URL here.

---

*Developed as an AI Developer assignment demonstrating Agentic AI concepts, automated policy validation, and enterprise workflow automation.*# hcltech-genai-case-study
