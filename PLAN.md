Step 1 — Plan
App: CreditReady
Pitch: Help Malaysian SMEs organize financing documents and see a clearly labeled demonstration of document-category coverage before approaching a financing provider.

Must-have features

SME and accounting-firm accounts, with role-specific dashboards.
SME business profile and private financial document uploads.
Six upload categories: financial statements, bank statements, tax documents, company documents, financing documents, and business documents.
Each upload receives a randomized 0-100% demonstration completeness value. The overall percentage averages all six categories equally; a category with no uploads counts as 0%, and no uploads means 0% overall. This is not based on file contents and is not a credit score.
Document checklist and financing-application preparation recommendations.
SMEs can explicitly share their business with a firm account; firms can only view businesses that granted access.
Preserve account security, CSRF protection, ownership checks, and the health check.
Nice-to-have, deferred

Real OCR or AI extraction, lender matching, bank/accounting integrations, payments, and subscriptions.
Database tables

users: id INTEGER, name TEXT, email TEXT UNIQUE, password_hash TEXT, role TEXT, account_status TEXT, created_at TEXT.
businesses: id INTEGER, owner_user_id INTEGER UNIQUE REFERENCES users(id) ON DELETE CASCADE, business_name TEXT, registration_number TEXT, business_type TEXT, contact_email TEXT, created_at TEXT.
documents: id INTEGER, business_id INTEGER REFERENCES businesses(id) ON DELETE CASCADE, uploaded_by INTEGER REFERENCES users(id) ON DELETE CASCADE, original_name TEXT, stored_name TEXT, document_type TEXT, completeness_percent INTEGER, processing_status TEXT, uploaded_at TEXT.
firm_clients: id INTEGER, firm_user_id INTEGER REFERENCES users(id) ON DELETE CASCADE, business_id INTEGER REFERENCES businesses(id) ON DELETE CASCADE, status TEXT, created_at TEXT. A relationship is active only after the SME grants access.
Pages and routes

/ — GET — CreditReady home page — No.
/register — GET, POST — Create an SME or firm account — No.
/login — GET, POST — Sign in and route to the relevant dashboard — No.
/logout — POST — Sign out — Yes.
/dashboard — GET — SME dashboard with document uploads and completeness percentages; firm users go to their dashboard — Yes.
/business/profile — GET, POST — Create or update the SME’s business profile — Yes, SME.
/documents/new — GET, POST — Upload one of six permitted document categories — Yes, SME.
/documents/<id>/download — GET — Download an authorized document — Yes, owner or authorized firm.
/documents/<id>/delete — POST — Delete an authorized document — Yes, owner.
/recommendations — GET — View missing categories and application-preparation steps — Yes, SME.
/business/share — POST — Grant a registered firm access to the SME’s business — Yes, SME.
/firm/clients — GET — List clients who granted access — Yes, firm.
/firm/clients/<business_id> — GET — View an authorized client’s documents and completeness percentages — Yes, authorized firm.
/health — GET — Return the existing health response — No.
Files to change

app.py
base.html, index.html, register.html, login.html, dashboard.html, business profile, document upload, recommendations, firm dashboard, and client detail templates
Remove the starter item form and manual financial-entry assessment templates.
style.css
test_app.py
No new package or deployment-file changes are planned.

Assumptions

CreditReady.html is mentioned as a visual reference but is not present in the workspace, so the existing starter templates are the available design reference.
The app does not read or grade document contents. Upload percentages are randomized independently for demonstration, and missing categories count as zero in the overall average.
SMEs grant access by entering a registered firm’s email. Payment processing, real integrations, and legal-compliance claims are out of scope for this prototype.
📌 Save this plan in a file called PLAN.md.