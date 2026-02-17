Name: Laura Bell Main 
Role: Lead Engineer - Application Security and Vulnerability Management

<!-- begin provided scenario and task content -->

## The Scenario

We are launching a new internal portal, and you have in this folder the beginnings of a login form. However, it currently lacks the necessary security measures to protect against common authentication based attacks. 

You are free to choose a development language, framework and/or tools of your choosing to complete this challenge. You are also free to use any AI assisted coding tools. However, if you do so, we require you to let us know what AI service and subsequent models were used during the completion of this project. 

## Objective
Enhance the existing login form to meet modern security standards.

## Tasks

You are tasked with implementing defenses against authentication based attacks. The following are some examples of measures that you may consider. These are neither mandatory nor comprehensive. You will use your expertise and experience to make a risk based decision balancing security controls vs the usability of the login form vs the time and resources you have at your disposal. :

1. Rate Limiting & Brute Force Protection to prevent credential stuffing and brute force attacks.
2. Secure Session Management to follow best practices (e.g., HttpOnly, Secure, SameSite, etc. flags) when setting session cookies and/or implement a secure "Logout" functionality that properly invalidates sessions server-side.
3. HTTP oriented security response headers (e.g., X-Frame-Options, Content-Security-Policy) specifically tailored to protect the login page from clickjacking and XSS.

<!-- end provided scenario and task content -->

## Assumptions

* Initial deployment is an internal facing portal. While this limits the breadth of variety in the end user profiles, I have assumed that all Xero employees may be required to use it and therefore it must be suitable for people with a range of technical experience levels and roles, across a range of geographies. As Xero values diversity, I will therefore assume that accessibility must be considered as part of this design and implementation.
* We do not have context to the criticality or sensitivity of the application that would be behind this login page. As such I will assume that the sensitivity of the provided functionality or data is of a commercially sensitive nature however unlikely to be a financial processing system or other critical system. If the associated functionality was more sensitive, additional controls may be recommended. See limitations and risks.
* I have assumed that regardless of whether something is deployed internally or externally, a high standard of engineering practice and security is required. I have also assumed that like many applications initially designed to be internal, this may be subject to change or external deployment with time.
* Where the recommended control would benefit from an additional architectural element, I have stated this as a suggestion however that is not provided in my solution. I have limited my provided solution to the controls that can be achieved in a short code implementation rather than a larger architectural design. 
* As a large software organization, I have assumed that some process is in place to vet 3rd party libraries and dependencies. As this is a short scoped exercise, I have assumed that the libraries used were already on an allow list of sorts and have not independently vetted them.

## Technical Choices

Given the nature of this assessment and the time limits, I have chosen intentionally lightweight frameworks and technologies that illustrate the objectives. 

* Language: Python (3.14)
* Framework: Flask
* Database: SQLlite
* Full requirements from package manager included in requirements.txt

## Functional Requirements
1. [ ] As a user, when providing a correct username but incorrect password, I should see a generic error message such as "Invalid username or password" so that I know my login failed without the system revealing which credential was wrong.
2. [ ] As a user, when providing an incorrect username, I should see the same generic error message and experience the same response time as for an incorrect password, so that my experience is consistent and my account security is protected.
3. [ ] As a user, when I make three or more incorrect login attempts, I should be informed that my account has been temporarily locked and given clear guidance on how to regain access (e.g. wait period or password reset), so that I understand what happened and what to do next.
4. [ ] As a user, when I provide a correct username and password, I should be authenticated and redirected to my intended destination securely, with a new session token issued, so that I can access the application without unnecessary friction.
5. [ ] As a user, when providing a correct username but incorrect password, I should not notice any difference in response time compared to an invalid username attempt, so that my experience remains consistent regardless of which field was incorrect.

## Non-functional Requirements
* Where error messages are provided to the user, they should not contain sensitive information
* The application must balance security and usability, as such, any brute force or rate limiting controls may be used to mitigate the risk of username enumeration. (In plain terms, it is better to be usable and have a useful error message if the brute force controls are mature as this will in turn reduce support tickets and required human intervention.)
* Where error messages or interfaces use colour to communicate meaning (such as warnings), this must also be done using other visual cues or words.

## Security Requirements

### Security Stories

#### Implemented
1. [ ] Passwords must be stored in the database in a secure manner (salted and hashed).
2. [ ] Passwords must never be visible in the system in plaintext.
3. [ ] Password hashes must not be transported outside the database or cross into the user interface.
4. [ ] Passwords must meet the security requirements of the defined Xero password policy (see assumptions).
5. [ ] The form must require both a username and password to authenticate.
6. [ ] The authentication request must be conducted over a secure (encrypted) connection. (see limitations)
7. [ ] Session identifiers should be protected and not accessible by JavaScript.
8. [ ] Any existing session identifiers must be revoked on submission of an authentication request.
9. [ ] A new session identifier should be generated and provided to the session on successful login.
10. [ ] Session identifiers should be generated by a high quality random number generator (as reviewed and approved) and be cryptographically secure pseudo-random.
11. [ ] Session duration should be clearly defined and configured (and suit the expected user behaviours and requirements for the application).

#### Not Implemented
1. [ ] All authentication activity must be logged.
2. [ ] The system should monitor for unusual activity (to be defined as by volume, resource usage, pattern of life or technologies) and take active measures to restrict or limit access. This activity should also be logged and alerts generated where appropriate to the supporting team.
3. [ ] Where session identifier/token length has not been predefined by the authorised framework, a suitable length should be defined that reduces the likelihood of automated generation and submission. This should be paired with the unusual session activity monitoring and brute force controls.
4. [ ] Any unusual activity (to be defined) in the session should revoke the session and force the user to re-authenticate

### Bad User Stories
1. [ ] As an attacker, when providing a correct username but incorrect password, I should not be able to determine that the username exists based on the error message, so that I cannot enumerate valid accounts.
2. [ ] As an attacker, when providing an incorrect username, I should receive the same generic error message as for an incorrect password, so that I cannot distinguish between invalid usernames and invalid passwords.
3. [ ] As an attacker, when attempting to send multiple authentication attempts to the application, I should be rate-limited or temporarily locked out after a defined number of failed attempts, so that I cannot brute-force credentials.
4. [ ] As an attacker, when providing either usernames or passwords to the authentication flow, I should not be able to inject malicious input (such as SQL injection or LDAP injection) that alters the authentication logic, so that I cannot bypass login controls.
5. [ ] As an attacker, when attempting to use an unencrypted transport protocol, I should be unable to transmit or intercept credentials over HTTP, because the application enforces HTTPS for all authentication traffic, so that I cannot capture credentials in transit.
6. [ ] As an attacker, when providing a correct username but incorrect password, I should not be able to infer validity through differences in response time, so that I cannot use timing-based side channels to enumerate accounts.


## Implementation Choices, Limitations and Risks
* Given the unknown criticality of the system, controls for more high risk systems such as financial processing applications were not implemented. This includes items listed for critical systems in ASVS and items such as multifactor authorisation. I have assumed that if we were building such a sensitive system we would probably use SSO rather than building authentication from scratch.
* Given the size and complexity of Xero, I have assumed that network level controls such as Web Application Firewalls and a centralised SIEM are in place and would be used in conjunction with code level controls for logging and monitoring.
* In the interests of time, I have included (in the code) how to turn on rudimentary ssl and Talisman for CORS, CSP, XSS and CSRF controls however I didn't have time to get the certificates sorted to get this up and running. I hope the intention is clear. In a working applictaion, I would have configured nginx or similar to handle this for me. The code has been included but commented out for this reason.
* CSS is not my strong suit so I have attempted to use and clean up the provided style sheet but I recommend a professional for this stuff.
* Password complexity checks are currently just set to length. Additional checks such as complexity, known to have been breached etc are available in the flask-security library but were not configured to allow for time.
* At this stage, error messages have been set to generic values that compromise user experience to reduce username enumeration risk. It is my opinion that this should be changed to more useful error messages when bruteforce controls and monitoring have been proven. This will improve user experience and reduce help requests.

## References

The following references were considered in the design of this solution:

* OWASP Application Security Verification Standard - version 5. (https://owasp.org/www-project-application-security-verification-standard/)
* Flask Security Documentation - https://flask-security-too.readthedocs.io/en/stable/index.html

## Use of AI Statement

While this exercise did permit the use of AI, I decided to do this manually to help my follow up discussions and as an excuse to refresh parts of my flask knowledge. 