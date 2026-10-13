# CreditReady Workflow Preparation Report

## 1. Purpose and scope

This report describes the CreditReady platform's current user workflows and the
preparation needed to operate, test, and extend them. It is based on the
application routes, data model, setup guide, and deployment configuration
currently in the repository.

The report separates implemented behavior from recommended operational
preparation. In particular, document completeness is currently randomized for
demonstration purposes, and uploaded files on Vercel are written to `/tmp`.
Those behaviors should not be treated as production document analysis or
persistent document storage.

## 2. Platform overview

CreditReady is a Flask web application that helps small and medium-sized
businesses organize information for financing-readiness discussions and lets
accounting firms review businesses that have granted them access.

The current application supports:

- SME and accounting-firm account registration and sign-in.
- Business-profile creation and editing for an SME account.
- Upload, download, and deletion of supported business documents.
- A dashboard summary of required document categories and recorded documents.
- Readiness-preparation recommendations.
- SME-controlled accounting-firm access grants and revocation.
- Firm client-list and client-detail views.
- SQLite for local development and PostgreSQL when `DATABASE_URL` is
  configured.

## 3. Roles and responsibilities

### SME user

- Creates an SME account and signs in.
- Maintains one business profile for the account.
- Uploads and manages the business's supporting documents.
- Reviews the dashboard and preparation guidance.
- Grants access to an existing accounting-firm account and can revoke it.

### Accounting-firm user

- Creates an accounting-firm account and signs in.
- Views businesses that have granted that firm access.
- Reviews permitted client details and associated readiness information.
- Does not grant itself access; access is initiated and revoked by the SME.

### Platform operator

- Configures the application secret and database connection for each
  environment.
- Verifies database availability, deployment health, and static asset delivery.
- Ensures document storage and privacy processes are appropriate for the
  environment before using real customer documents.
- Maintains database backups, access procedures, and incident response outside
  the application itself.

## 4. Primary user workflows

### 4.1 Visitor registration and sign-in

1. A visitor opens the landing page.
2. The visitor chooses registration and selects either the SME or accounting
   firm role.
3. The application validates the name, email address, role, and password.
4. The application creates the account with a password hash; duplicate email
   addresses are rejected.
5. The visitor is directed to sign in.
6. On successful sign-in, SME users are sent to the SME dashboard and firm
   users to the firm client list.
7. Signing out clears the session and returns the user to the landing page.

Operational checks:

- Confirm email uniqueness and role selection are understandable to users.
- Use a strong, environment-specific `SECRET_KEY`; do not rely on the
  development fallback in a deployed environment.
- Confirm session behavior and HTTPS settings on the production domain.

### 4.2 SME business-profile setup

1. An SME signs in and opens the dashboard.
2. If no business profile exists, the SME is prompted to create one.
3. The SME enters the business name, registration number, business type, and
   contact email.
4. The application validates required values and saves the profile.
5. The SME returns to the dashboard, where document and readiness sections
   can be populated.

The current data model permits one business profile per SME account. Confirm
that this matches the intended account model before onboarding users with
multiple businesses.

### 4.3 Document preparation and management

1. The SME opens the document-upload workflow.
2. The SME selects a document category and uploads a PDF, PNG, JPG, or JPEG.
3. The application validates the category, file name, extension, signature,
   and maximum upload size.
4. A generated storage name is used, and the document record is associated
   with the SME's business profile.
5. The dashboard lists the document and its category.
6. The SME or an authorized accounting-firm user can download permitted
   documents; the SME can delete the SME-owned document.

Current document categories are financial statements, bank statements, tax
documents, company documents, financing documents, and business documents.
The maximum upload size is 10 MB.

Important operational limitation: completeness is currently assigned a random
percentage for demo purposes; it is not computed by inspecting the document.
Also, Vercel deployments write uploads to `/tmp`, which is temporary serverless
storage and may be cleared between invocations or deployments. Do not rely on
these files being durable. Before production use, choose and implement
persistent private object storage, define retention and deletion behavior, and
ensure database records cannot point to missing files.

### 4.4 Readiness review

1. The SME reviews the dashboard's document categories and recorded uploads.
2. The SME opens the recommendations page.
3. The application presents preparation guidance, including gathering recent
   financial statements and bank statements, company-registration information,
   loan details, and a cash-flow forecast.
4. The SME uses the guidance to prepare material for an external financing
   conversation.

The current recommendations are general preparation guidance. They should not
be represented as a lending decision, credit approval, underwriting result,
financial advice, or verified analysis of uploaded files.

### 4.5 SME-to-firm access sharing

1. The SME enters the email address associated with an existing firm account.
2. The application verifies that the account exists and has the firm role.
3. The application creates or reactivates the relationship between the firm and
   the SME's business.
4. The firm sees the business in its client list and can open its permitted
   details.
5. The SME can revoke an active grant from the dashboard.
6. A revoked relationship no longer authorizes access to the client detail
   view.

Operational checks:

- Explain what profile information and documents are visible before access is
  granted.
- Test that one firm's grant cannot expose another firm's client data.
- Test access immediately after revocation, including direct URLs and document
  download requests.
- Maintain an auditable record of grant, reactivation, and revocation events if
  required by the platform's operating policy; the current relationship record
  is not a complete audit log.

## 5. Route and access overview

| User journey | Application route | Expected access |
| --- | --- | --- |
| Landing page | `/` | Public |
| Registration | `/register` | Public |
| Sign-in | `/login` | Public |
| Sign-out | `/logout` | Session action |
| SME dashboard | `/dashboard` | Signed-in user; firm users are redirected |
| Business profile | `/business/profile` | SME |
| New document | `/documents/new` | SME |
| Download document | `/documents/<id>/download` | Signed-in user with access |
| Delete document | `/documents/<id>/delete` | Owning SME |
| Recommendations | `/recommendations` | SME |
| Firm client list | `/firm/clients` | Accounting firm |
| Grant firm access | `/business/share` | SME |
| Revoke firm access | `/business/share/<grant_id>/revoke` | SME that owns the business |
| Firm client detail | `/firm/clients/<business_id>` | Firm with active access |
| Health check | `/health` | Operational probe |

All state-changing form submissions should include the application's CSRF
token. Continue validating authorization at the resource level rather than
assuming that a signed-in user may access an arbitrary business or document
identifier.

## 6. Data lifecycle

The current relational model includes:

- **Users:** email/username, display name, role, account status, password hash,
  and creation time.
- **Businesses:** owner, business name, registration number, business type,
  contact email, and creation time.
- **Documents:** business, uploader, original and generated names, category,
  demo completeness percentage, processing status, and upload time.
- **Firm-client relationships:** firm, business, active/revoked status, and
  relationship timestamp.

The application initializes or migrates its schema during app creation. Local
development defaults to SQLite. A Vercel deployment requires a non-empty
`DATABASE_URL`, which is stripped of surrounding whitespace before use.

Preparation recommendations:

1. Keep database credentials in deployment environment variables, never in
   source control.
2. Select and document the intended PostgreSQL connection method and pool
   limits for the hosting provider.
3. Test schema initialization and application startup against a non-production
   database before deploying.
4. Define backup, restore, retention, and account-removal procedures.
5. Treat account and document data as sensitive, and restrict production
   database access to the minimum necessary operators.

## 7. Environment and deployment workflow

### Local development

1. Create and activate a project virtual environment.
2. Install `requirements-dev.txt` to include runtime and test dependencies.
3. Run the Flask app with `python app.py`.
4. Open the local development URL and exercise SME and firm journeys.
5. Run the automated test suite with `python -m pytest`.

Local development uses SQLite when `DATABASE_URL` is blank. Uploaded files are
stored under the local `instance/private_uploads` directory.

### Vercel deployment

1. Configure `SECRET_KEY` and `DATABASE_URL` as server-side environment
   variables for the correct Vercel environment.
2. Deploy the Python function at `api/index.py`, which exposes the app created
   by the root `app.py` factory.
3. Route incoming paths to the Flask function and ensure static files under
   `/static/` are included and served correctly.
4. Verify `/`, `/health`, a rendered page's CSS, and a representative
   authenticated flow after deployment.
5. Confirm production database connectivity and exercise the deployed schema.
6. Verify persistent private document storage before relying on uploads.

The root factory anchors the template and static directories to the root
application path. `DATABASE_URL` is required when Vercel is detected, and the
upload directory is `/tmp`; the latter is suitable only for temporary
serverless files, not as durable document storage.

## 8. Release validation checklist

### Functional

- [ ] Landing page, registration, sign-in, and sign-out work.
- [ ] SME and firm roles land on the correct dashboards.
- [ ] SME can create and update a valid business profile.
- [ ] Supported document uploads pass validation; unsupported or oversized
      files are rejected with a clear message.
- [ ] SME can download and delete its own documents.
- [ ] Dashboard and recommendations render when a business has no documents
      and when it has documents.
- [ ] Firm can see only businesses with active access grants.
- [ ] Revocation immediately blocks firm detail and document access.
- [ ] The CSS file and other intended static assets return successfully.

### Security and privacy

- [ ] Production secret values are unique, strong, and not committed.
- [ ] CSRF protection is enabled for state-changing requests.
- [ ] Passwords are stored as hashes, not plaintext.
- [ ] Object-level access checks prevent cross-business access.
- [ ] Upload type, signature, size, and filename validation are exercised.
- [ ] Sensitive uploads are stored privately and are not exposed through public
      static routes.
- [ ] Sharing and revocation behavior is explained to users.
- [ ] Logs and error responses do not disclose credentials or sensitive data.

### Operational

- [ ] Production database connection and schema startup are verified.
- [ ] `/health` returns the expected healthy response.
- [ ] Database backups and restore procedures are tested.
- [ ] Persistent document storage, retention, and deletion are verified.
- [ ] Monitoring and error reporting are configured for the production
      environment.
- [ ] Deployment environment variables are present for Preview and Production
      as intended.

## 9. Known gaps and next preparation steps

1. **Persistent file storage:** replace Vercel `/tmp` as the durable file store
   with private object storage and define a safe migration/retention approach.
2. **Real document assessment:** replace the random completeness percentage
   with a documented, testable assessment process before presenting scores as
   meaningful.
3. **Auditability:** decide whether access grants, revocations, downloads, and
   administrative actions require an append-only audit history.
4. **Production policy:** define privacy notice, consent, retention, deletion,
   support, and incident-response procedures for financial documents.
5. **Role and access testing:** add focused tests for firm isolation, SME
   ownership, revoked grants, and inaccessible resources.
6. **Operational readiness:** establish production monitoring, database
   recovery drills, environment-variable review, and a release checklist.
7. **User expectations:** clearly state that readiness guidance is preparatory
   and does not guarantee financing or replace professional advice.

## 10. Workflow success criteria

The platform is ready for a controlled workflow pilot when an SME can create an
account, maintain a business profile, upload and manage documents in persistent
private storage, understand the limits of the readiness guidance, and grant or
revoke access with confidence—and when an accounting firm can access only
currently authorized client information. Operators should be able to deploy,
monitor, back up, and restore the application without depending on local or
serverless temporary files.
