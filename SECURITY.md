# 🔐 Security Policy

This repository contains synthetic HR data and local analytics utilities. It must never contain production credentials, real employee information or confidential organisational records.

## Supported version

Security and privacy fixes are applied to the latest commit on `main`.

## Report a vulnerability privately

1. Open the repository **Security** tab.
2. Select **Advisories** → **Report a vulnerability** when private vulnerability reporting is available.
3. Include the affected file, impact, reproduction steps and a safe proof of concept.

Do **not** publish exploit details, credentials, real personal data or confidential files in a public issue. When the private form is unavailable, open a public issue that only asks the maintainer to establish a private contact channel; do not include vulnerability details.

## Security scope

Please report:

- exposed credentials, access tokens or private keys;
- real employee, applicant, payroll, health or confidential organisational data;
- path traversal or unsafe file handling;
- spreadsheet-formula injection in CSV files;
- malicious or hidden notebook execution;
- macro, ActiveX or embedded-object content in Excel workbooks;
- vulnerable Python dependencies;
- unsafe GitHub Actions permissions or supply-chain risks;
- any practical method to alter, execute or exfiltrate data unexpectedly.

## Maintainer response

The maintainer aims to:

- acknowledge a valid private report within two business days;
- assess severity and affected versions;
- prepare a focused fix without exposing the issue prematurely;
- run repository validation, dependency auditing and CodeQL checks;
- document the resolution after the fix is available.

## Responsible disclosure

Please allow reasonable remediation time before public disclosure. Reports that contain real personal data should include only the minimum evidence needed for verification.

## Existing controls

- read-only workflow permissions by default;
- CodeQL analysis with extended security queries;
- automated Python dependency auditing;
- Dependabot updates for Python and GitHub Actions;
- repository validation for path containment, CSV formula injection, passive notebooks and bounded XLSX archives;
- ignored credential, token and private-key file patterns.
