# Our Project Idea

## 1. App name

CreditReady

## 2. Team

| Name | Role |
|---|---|
| jian hao | Team Lead / Project Coordination |
| jian hao | Backend Development |
| guan yu | Frontend / UI/UX Design |
| guan yu | Testing and Documentation |

## 3. The problem (2–3 sentences)

Many Malaysian small and medium-sized enterprises (SMEs) find it difficult to determine whether they are financially ready to apply for a business loan. Their financial statements, bank statements, and supporting documents may contain missing or inconsistent information, making it harder to understand their financial position and prepare a strong financing application. CreditReady aims to help SMEs identify their financial strengths and weaknesses before applying, so they can address potential issues and approach financing providers with greater confidence.

## 4. Who uses the app?

The main users are Malaysian SMEs that want to assess their credit readiness before applying for business financing. A second group consists of accounting and audit firms that want to provide credit-readiness assessments and advisory services to their SME clients.

- **SME users:** Upload financial documents, view a randomized document-completeness estimate, identify missing document categories, and receive application-preparation guidance.
- **Accounting and audit firms:** Manage multiple authorized SME client files, review uploaded documents and their demonstration completeness estimates, and offer advisory services.
- **Future users:** Banks and financial institutions may be integrated in later development phases to support financing workflows.

The platform is not a lender and does not make final lending decisions. Different user types should have different access permissions. SMEs should only access their own information, while accounting firms should only access client information they are authorised to manage. Bank integrations and advanced firm-management functions may be developed in later phases.

## 5. Must-have features (3–6)

1. **User registration and login:** Allow SME users and accounting firms to create accounts, log in, and access the appropriate features for their roles.

2. **Financial document upload:** Allow users to upload financial statements, bank statements, and supporting documents for credit-readiness assessment. The system should validate uploaded files and display clear error messages when a document is missing or cannot be processed.

3. **Document completeness demonstration:** Support financial statements, bank statements, tax documents, company documents, financing documents, and business documents. Randomly assign each upload a percentage for demonstration; do not claim to read, extract, or grade document contents.

4. **Document-completeness dashboard:** Average upload percentages within each category, then average the six category percentages equally. Categories with no uploads count as 0%, so a business with no uploads has an overall estimate of 0%. Clearly label this randomized demonstration estimate; it is not a credit score or a measure of actual file quality.

5. **Recommendations and application preparation:** Show missing document categories and a practical checklist of information commonly prepared for a financing application.

6. **Accounting firm dashboard:** Allow authorized accounting and audit firms to view client profiles and document-completeness summaries only after the SME grants access. Access to each client's documents must be restricted to authorized users.

## 6. Nice-to-have features (only if there's time)

1. **Financing options and lender matching:** Show suitable financing options based on the SME's profile and credit-readiness results. This should be introduced as a later-stage feature and must not imply that financing is approved.

2. **Bank and accounting software integrations:** Integrate with banks, accounting software, and other relevant financial data providers to reduce manual document uploads and improve the efficiency of financial analysis. A mobile application could also be introduced in a future phase.

## 7. What data do we save?

- **User account:** User ID, name, email address, securely hashed password, user role (SME or accounting/audit firm), account status, and registration details.
- **Business / SME profile:** Business name, business identification details where required, business type, contact information, and relevant financial profile information.
- **Financial documents:** Uploaded financial statements, bank statements, tax documents, company documents, financing documents, business documents, upload date, randomized demonstration completeness percentage, processing status, and access permissions.
- **Document completeness summary:** Per-category average percentages and an overall average across all six categories; categories without uploads count as 0%.
- **Accounting firm profile:** Firm name, authorised user accounts, subscription plan, and client relationships.
- **Client access permissions:** The SME or client associated with an accounting firm, the authorised users, and the level of access granted.
- **Financing preparation record:** Relevant financing requirements, selected financing options if this feature is implemented, application preparation status, and any associated recommendations.
- **Subscription and payment records:** Subscription type, payment status, billing period, and report purchases for accounting firms using paid features.

Sensitive financial documents and extracted data must be stored securely. Only collect information needed for the application's functions, and do not store actual account passwords in plain text.

## 8. Is data private or shared?

Financial documents, document-completeness estimates, and recommendations are private business information. SME users should only be able to access their own business records. Accounting and audit firms may access an SME's information only when the SME has authorized that access or another valid permission has been established.

The system must enforce permissions on the backend, not merely hide information on the interface. Users must not be able to access another business's documents or reports by changing a URL or record ID.

The application should be designed with Malaysia's Personal Data Protection Act (PDPA) requirements in mind, including appropriate data handling, access controls, and protection of sensitive business information. The project should not claim full legal compliance until the necessary requirements have been reviewed and implemented.

CreditReady provides credit-readiness guidance and application preparation; it is not a lender and does not guarantee loan approval. Financial information should not be shared publicly. Any future integrations with lenders or third-party service providers should require appropriate permissions and safeguards.

## 9. Pages we want

1. **Home / Landing Page:** Introduce CreditReady, explain its benefits, show how the platform works, and provide navigation to the dashboard, sign-up, login, and accounting firm section.
2. **Sign Up:** Allow SMEs and accounting/audit firms to register using the appropriate account type.
3. **Log In:** Authenticate registered users and direct them to the correct dashboard based on their role.
4. **SME Dashboard:** Display the randomized document-completeness estimate, per-category percentages, uploaded files, missing categories, and application-preparation steps.
5. **Document Upload:** Allow users to upload all six document categories and view each upload's randomized demonstration percentage.
6. **Document Checklist and Preparation:** Show which categories have uploads and a practical financing-application preparation checklist.
7. **Accounting Firm Dashboard:** Allow authorized firms to view multiple client files only when each SME has granted access.
8. **Client Details:** Display the selected client's authorized business information, uploaded documents, and randomized completeness estimates.
10. **Account Settings:** Allow users to manage their account details, security settings, and relevant preferences.
11. **Subscription / Pricing Page:** Explain the firm's subscription and report-fee structure. Payment processing can be implemented later if required.
12. **Financing Options Page:** A future page for presenting potentially suitable financing options or lender integrations.

## 10. Look and feel

- **Main colour (hex or name):** Use the existing CreditReady HTML design as the reference. Preserve its established colour palette where possible; the exact primary colour should be confirmed from the CSS variables in the original file.
- **Style words:** Professional, modern, clean, trustworthy, accessible, finance-focused, and responsive.
- **Layout:** Use clear sections, cards, dashboards, readable financial summaries, and consistent spacing.
- **Data visualisation:** Use progress bars for clearly labelled document-completeness demonstration percentages, not credit scores.
- **Navigation:** Provide straightforward navigation between the home page, SME dashboard, document upload, assessment results, and accounting firm dashboard.
- **Responsive design:** Ensure that the interface works on desktop, tablet, and mobile screens.
- **User experience:** Use plain language to explain financial terms, display clear upload and processing statuses, and provide helpful messages when information is missing or an assessment cannot be completed.
- **Accessibility:** Use readable font sizes, sufficient colour contrast, keyboard-friendly controls, and clear form labels.

The existing `CreditReady.html` should be treated as the primary visual reference. Reuse its design patterns and existing working interactions where appropriate rather than replacing the design without reason.

## 11. Anything else the AI should know

- **Build on the existing project:** Inspect the existing starter code, project structure, dependencies, templates, styles, and tests before changing anything. Reuse suitable existing components and preserve working functionality.
- **Use the existing CreditReady prototype:** Treat the uploaded `CreditReady.html` as the reference for the product concept, page structure, wording, colour palette, and visual style. Do not replace the CreditReady concept with another application idea.
- **Implement incrementally:** First explain the existing project structure and propose a development plan. Divide implementation into small stages, test each stage, and avoid rewriting the entire project at once.
- **Prioritise the core workflow:** Start with account access, secure document upload, financial data extraction, assessment results, recommendations, and the SME dashboard. Implement accounting firm client management after the core SME workflow is working.
- **Technology:** Follow the existing starter project's framework and database technology. Do not introduce a new framework or database without a clear reason.
- **AI and OCR:** Real extraction is out of scope for this prototype. Do not collect manual financial figures to generate a credit score or present randomized document percentages as actual OCR results.
- **Financial accuracy:** Do not claim files have been read or graded. Explain that per-upload percentages are randomized for demonstration and do not measure actual document quality or predict a lender's decision.
- **Security:** Protect uploaded documents, passwords, financial data, assessment reports, and client records. Enforce authorisation on the server, validate uploads, and avoid exposing sensitive information in logs or public pages.
- **Testing:** Add automated tests for registration, login, document uploads, access permissions, financial-data processing, assessment generation, and accounting firm access to client files.
- **Business model:** The prototype describes a firm subscription of RM800 per month, a credit-readiness report fee of RM150 per report, and a premium add-on of RM300 per month. It also mentions a 50% pilot discount for the first five firms in Q1 and free SME access through accountants during Year 1. Treat these as proposed pricing assumptions, not completed payment functionality.
- **Market information:** The HTML prototype includes Malaysian SME market figures and references to Bank Negara Malaysia and DOSM. Verify these figures and their sources before using them in a live application or formal business report.
- **Development roadmap:** Phase 1 focuses on accounting and audit firms and a pilot; Phase 2 may introduce bank integrations, financial institution partnerships, and a mobile application.
- **Definition of done:** An authorized SME can upload documents in all six categories, see each upload's randomized demo percentage, and see an overall percentage that is 0% when there are no uploads and includes missing categories as zero. An authorized accounting firm can view permitted client files without accessing unrelated businesses' information. Automated tests should pass before the core features are considered complete.

---