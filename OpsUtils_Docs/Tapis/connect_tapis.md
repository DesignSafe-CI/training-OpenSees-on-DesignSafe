# connect_tapis()
***connect_tapis(token_filePath="~/.tapis_tokens.json", base_url="https://designsafe.tapis.io", username="", password="", force_connect=False)***

**Purpose.** Create an authenticated **Tapis** client (e.g., for DesignSafe) with **automatic token handling**. It reuses a valid saved token when available, otherwise securely prompts for credentials, fetches a new token, saves it for next time, and returns a ready‑to‑use client.

---

### What it does

* **Checks** *token_filePath* (default *~/.tapis_tokens.json*) for a saved token.
* **Valid token** → uses it directly (no login prompts).
* **Missing/expired or *force_connect=True*** → prompts for credentials, **gets new tokens**, and **saves** them back to *token_filePath*.
* **Prints** when the token expires and how long remains.

---

### Parameters

* *token_filePath* *(str, default *"~/.tapis_tokens.json"*)* – Path to the JSON token file.
* *base_url* *(str, default *"https://designsafe.tapis.io"*)* – Tapis API base URL.
* *username* *(str, default *""*)* – Preset username; if empty, you’ll be prompted.
* *password* *(str, default *""*)* – Preset password; if empty, you’ll be prompted securely.
* *force_connect* *(bool, default *False*)* – Force a fresh login even if a valid token exists.

---

### Returns

* **Tapis client** – An authenticated *Tapis* object; use it immediately for jobs, files, systems, etc.

---

### Token file format (JSON)

```json
{
  "access_token": "…",
  "expires_at": "2025-08-31T12:34:56+00:00"
}
```

*Timezone is handled; naive timestamps are treated as UTC.*

---

### Example

```python
# Use a saved token if valid; otherwise prompt and save a new one
t = connect_tapis()

# You're now authenticated:
jobs = t.jobs.getJobList()
for j in jobs:
    print(j.id, j.status)
```

---

### Notes & tips

* **Security:** The token file contains only the access token and expiry, not your password.
* **Portability:** You can point *token_filePath* to a project‑specific location (e.g., inside a workspace).
* **Refreshing early:** Set *force_connect=True* to rotate tokens proactively.

---

#### Files

You can find these files in Community Data.

```{dropdown} connect_tapis.py
:icon: file-code
```{literalinclude} ../../OpsUtils/OpsUtils/Tapis/connect_tapis.py
:language: none
```

---

**Author:** Silvia Mazzoni, DesignSafe ([silviamazzoni@yahoo.com](mailto:silviamazzoni@yahoo.com))
**Date:** 2025-08-14
**Version:** 1.0
