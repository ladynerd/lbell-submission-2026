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
* We do not have context to the criticaility or sensitivity of the application that would be behind this login page. As such I will assume that the sensitivity of the provided functionality or data is of a commercially sensitive nature however unlikely to be a financial processing system or other critical system. If the associated functionality was more sensitive, additional controls may be recommended. See limitations and risks.
* I have assumed that regardless of whether something is deployed internally or externally, a high standard of engineering practice and security is required. I have also assumed that like many applications initially designed to be internal, this may be subject to change or external deployment with time.
* Where the recommended control would benefit from an additional architectural element, I have stated this as a suggestion however that is not provided in my solution. I have limited my provided solution to the controls that can be achieved in a short code implementation rather than a larger architectural design. 

## Technical Choices

Given the nature of this assessment and the time limits, I have chosen intentionally lightweight frameworks and technologies that illustrate the objectives. 

Language: Python
Framework: Flask
Database: SQLlite



## Functional Requirements
As a user, when providing a correct username but incorrect password, ...
As a user, when providing an incorrect username , ...
As a user, when I make three or more incorrect login attempts, ...
As a user, when I provide a correct username and password, ...
As a user, when providing a correct username but incorrect password, ...

## Non-functional Requirements
* Where error messages are provided to the user, they should not contain sensitive information
* The application must balance security and useability, as such, any brute force or rate limiting controls may be used to mitigate the risk of username enumeration. (In plain terms, it is better to be usable and have a useful error message if the brute force controls are mature as this will in turn reduce support tickets and required human intervention.)
* Where error messages or interfaces use colour to communicate meaning (such as warnings), this must also be done using other visual cues or words.

## Security Requirements

### Security Stories

#### Implemented
* All authentication activity must be logged.
* Passwords must be stored in the database in a secure manner (salted and hashed).
* Passwords must never be visible in the system in plaintext.
* Password hashes must not be transported outside the database or cross into the user interface.
* Passwords must meet the security requirements of the defined Xero password policy (see assumptions).
* The form must require both a username and password to authenticate.
* The authentication request must be conducted over a secure (encrypted) connection.
* Session identifiers should be protected and not accessible by JavaScript.
* Any existing session identifiers must be revoked on submission of an authentication request.
* A new session identifier should be generated and provided to the session on successful login.
* Session identifiers should be generated by a high quality random number generator (as reviewed and approved) and be cryptographically secure pseudo-random.
* Session duration should be clearly defined and configured (and suit the expected user behaviours and requirements for the application).

#### Not Implemented
* The system should monitor for unusual activity (to be defined as by volume, resource usage, pattern of life or technologies) and take active measures to restrict or limit access. This activity should also be logged and alerts generated where appropriate to the supporting team.
* Where session identifier/token length has not been predefined by the authorised framework, a suitable length should be defined that reduces the likelihood of automated generation and submission. This should be paired with the unusual session activity monitoring and brute force controls.
* Any unusual activity (to be defined) in the session should revoke the session and force the user to re-authenticate

### Bad User Stories

As an attacker, when providing a correct username but incorrect password, ...
As an attacker, when providing an incorrect username , ...
As an attacker, when attempting to send multiple authentication attempts to the application, ...
As an attacker, when providing either usernames or passwords to the authentication flow, ...
As an attacker, when attempting to use an unencrypted transport protocol, ...
As an attacker, when providing a correct username but incorrect password, ...



## Implementation Choices, Limitations and Risks
* Given the unknown criticality of the system, controls for more high risk systems such as financial processing applucations were not implemented. This includes items listed for critical systems in ASVS and items such as multifactor authorisation. I have assumed that if we were building such a sensitive system we would probably use SSO rather than building authentication from scratch.


## References

The following references were considered in the design of this solution:

* OWASP Application Security Verification Standard - version 5. (https://owasp.org/www-project-application-security-verification-standard/)
