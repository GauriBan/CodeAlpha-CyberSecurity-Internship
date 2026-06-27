# Secure Coding Review

## Application Reviewed
Basic Network Sniffer (Python)

## Objective
Review the source code to identify security issues and suggest improvements.

## Findings
1. No input validation.
2. No exception handling.
3. No logging mechanism.
4. Requires administrator privileges.
5. Packet data is not stored securely.

## Recommendations
- Add try-except blocks.
- Use proper logging.
- Validate user inputs.
- Run with minimum required privileges.
- Store captured data securely.

## Author
Gauri 