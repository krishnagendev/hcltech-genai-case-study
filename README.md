# Travel Reimbursement Approval Agent
### Agentic AI-Based Expense Validation and Approval System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Agentic AI](https://img.shields.io/badge/AI-Agentic%20AI-purple)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter%20Notebook-orange)
![Status](https://img.shields.io/badge/Status-Working%20Prototype-success)

## 1. Project Overview

The **Travel Reimbursement Approval Agent** is a Python-based Agentic AI prototype designed to automate employee travel expense validation and reimbursement decisions.

The system evaluates employee reimbursement claims against predefined company policies, validates supporting receipts, checks expense limits, detects potential duplicate transactions, and determines the appropriate approval status.

It combines an agent orchestration workflow, specialized validation tools, deterministic business rules, and optional OpenAI Function Calling for intelligent tool selection.

The solution also supports human-in-the-loop review for exceptional, incomplete, or high-risk claims.

## 2. Business Problem Statement

Traditional travel reimbursement processing involves several manual activities:

- Checking expense eligibility against company policies.
- Validating receipts and supporting documents.
- Verifying meal, accommodation, and transportation limits.
- Identifying duplicate expense transactions.
- Checking reimbursement submission deadlines.
- Routing exceptional or high-value claims for manual approval.

These activities increase processing time and can result in inconsistent decisions and operational overhead.

**Objective:** Build an automated reimbursement validation system that improves decision consistency, reduces manual effort, and provides transparent, policy-based reimbursement decisions.

## 3. Solution Architecture and Agent Workflow

The solution follows a modular, tool-based agent orchestration approach.

### Workflow

1. **Claim Intake:** Accept employee travel reimbursement claims.
2. **Policy Lookup:** Retrieve applicable reimbursement policies and rules.
3. **Receipt Validation:** Verify mandatory supporting documents.
4. **Expense Validation:** Check eligible expense categories and reimbursement limits.
5. **Timeliness Validation:** Verify compliance with the 30-day submission policy.
6. **Duplicate Detection:** Identify potential duplicate expense entries.
7. **Approval Threshold Validation:** Determine the applicable approval level.
8. **Decision Engine:** Evaluate validation results and generate the reimbursement decision.
9. **Output Validation:** Validate the structured JSON response.
10. **Audit and Reporting:** Record tool execution results and generate dashboard visualizations.

### Supported Decision Types

| Decision | Description |
|---|---|
| APPROVE | All evaluated expenses satisfy applicable policies |
| PARTIAL_APPROVE | Eligible expenses are approved while deductions are applied |
| REJECT | The claim contains expenses that fail mandatory policy conditions |
| MANUAL_REVIEW | The claim requires human verification or approval |

## 4. Dataset and Test Scenarios

The project uses five sample employee reimbursement claims provided as part of the assignment.

| Claim ID | Business Scenario |
|---|---|
| CLM-001 | Industry conference travel |
| CLM-002 | Weekend hotel stay |
| CLM-003 | Client site visit |
| CLM-004 | International vendor negotiation |
| CLM-005 | Client dinner / business development |

The sample dataset contains employee details, business purpose, travel dates, expense categories, claimed amounts, and receipt availability.

A Python-based policy knowledge base maintains reimbursement rules and policy references used during validation.

## 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Jupyter Notebook | Development and execution environment |
| Pandas | Data processing and analysis |
| Matplotlib | Dashboard and data visualization |
| OpenAI Function Calling (Optional) | Intelligent tool selection |
| JSON | Structured input and output |
| Rule-Based Decision Engine | Deterministic policy validation |
| Agent Orchestration | Coordinating validation tools |
| IPython | Interactive notebook execution |

## 6. Key Features

- Automated travel reimbursement claim evaluation.
- Policy-based expense validation.
- Receipt and supporting document verification.
- Expense category and spending limit validation.
- Submission deadline verification.
- Potential duplicate expense detection.
- Approval threshold evaluation.
- Human-in-the-loop exception handling.
- Structured JSON decision generation.
- Agent tool execution audit trail.
- Dashboard-based reimbursement reporting.

## 7. Reimbursement Decision Results

The system evaluates all five sample reimbursement claims.

| Claim ID | Decision | Key Finding |
|---|---|---|
| CLM-001 | APPROVE | Expenses comply with applicable reimbursement policies |
| CLM-002 | REJECT | Contains ineligible spa and minibar expenses |
| CLM-003 | PARTIAL_APPROVE | Lodging expense exceeds the permitted limit |
| CLM-004 | MANUAL_REVIEW | Business-class airfare, missing receipt, and high-value claim |
| CLM-005 | MANUAL_REVIEW | Mandatory meal receipt is missing |

These results demonstrate the system's ability to distinguish between eligible, partially eligible, rejected, and exceptional reimbursement claims.

## 8. Dashboard and Output

The application generates:

- Claim-wise reimbursement decision summaries.
- Approved and deducted amount calculations.
- Missing document identification.
- Policy reference tracking.
- Agent tool execution audit logs.
- Dashboard visualizations of decision distribution and financial summaries.

### Structured JSON Output

The system produces a structured JSON response containing nine required fields:

1. `claim_id`
2. `decision`
3. `approved_amount`
4. `deducted_amount`
5. `missing_documents`
6. `policy_references`
7. `confidence`
8. `explanation`
9. `tools_used`

This structured output supports downstream integrations, reporting, auditability, and future enterprise workflow automation.

## 9. Installation and Execution

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Git (optional, for repository management)

### Step 1: Clone the Repository

```bash
git clone https://github.com/krishnagendev/hcltech-genai-case-study.git
```

### Step 2: Navigate to the Project Directory

```bash
cd hcltech-genai-case-study
```

### Step 3: Install Dependencies

```bash
pip install notebook pandas matplotlib ipython
```

### Step 4: Launch Jupyter Notebook

```bash
jupyter notebook
```

### Step 5: Open the Project Notebook

Open:

`Travel_Reimbursement_Approval_Agent.ipynb`

### Step 6: Execute the Notebook

Select:

`Kernel → Restart & Run All`

Alternatively, upload the notebook to Google Colab and select:

`Runtime → Run all`

### Step 7: Review the Results

After execution, review:

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

Configure the `OPENAI_API_KEY` environment variable before starting Jupyter Notebook.

Without an API key, the application uses its local rule-based tool planner.

**Security Note:** Never commit API keys, credentials, or `.env` files to the GitHub repository.

## 10. Technical Highlights

The project demonstrates practical implementation of:

- Python-based agent orchestration.
- Tool-based execution and validation.
- Deterministic business rule evaluation.
- Policy-driven decision-making.
- Structured JSON response generation.
- Exception handling and human-in-the-loop routing.
- Audit logging and reporting.

The architecture separates business policy validation from tool orchestration, making the solution easier to maintain, test, and extend.

## 11. Future Enhancements

The following enhancements can extend the current prototype toward production readiness:

| Enhancement | Proposed Implementation |
|---|---|
| Stateful Agent Orchestration | LangGraph |
| LLM Integration | Azure OpenAI |
| Receipt Processing | Azure AI Document Intelligence |
| Policy Retrieval | RAG with Azure AI Search |
| Human-in-the-Loop | Manager approval workflow |
| Persistent Storage | SQL Database / Azure Cosmos DB |
| API Development | Python FastAPI |
| Cloud Deployment | Microsoft Azure |
| Monitoring | Application Insights and structured logging |
| Evaluation | Agent execution and decision accuracy metrics |

## 12. Conclusion

The Travel Reimbursement Approval Agent demonstrates how Agentic AI concepts and Python-based automation can simplify enterprise travel reimbursement processing.

By combining policy lookup, specialized validation tools, deterministic decision-making, structured JSON responses, and human-in-the-loop review, the solution provides a transparent and auditable reimbursement workflow.

The project demonstrates the practical application of AI agents in enterprise business process automation, with a modular foundation for future integration with LLMs, RAG, LangGraph, and Azure AI services.

## 13. Project Information

**Author:** Krishna Kumar

**Project:** Travel Reimbursement Approval Agent

**Technical Focus:** Python | Generative AI | Agentic AI | LLMs | Automation

**Email:** kknup2609@gmail.com

**Location:** Pune, India

**GitHub Repository:**  
https://github.com/krishnagendev/hcltech-genai-case-study

---

*Developed as an AI Developer technical assignment to demonstrate Agentic AI concepts, automated policy validation, tool orchestration, and enterprise workflow automation.*
