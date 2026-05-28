# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in cozy-kit, please report it responsibly.

Please do not publicly disclose security vulnerabilities before they are reviewed and addressed.

You can report vulnerabilities by:

* Opening a private GitHub security advisory
* Contacting the maintainer directly through GitHub

## What Counts as a Security Issue?

Examples may include:

* Dangerous code execution
* Dependency vulnerabilities
* Unsafe file or system access
* Malicious package behavior

Normal bugs, crashes, or feature requests should be reported through GitHub Issues instead.

## Example of a Security Issue

For example:

```python
eval("1 + 1")
```

This is generally harmless and returns:

```python
2
```

However, something like:

```python
__import__("os").system("something")
```

could potentially execute dangerous system commands on the computer.

Thank you for helping improve the security and quality of cozy-kit.
