<!-- # Tapis Tokens
**Tapis Authentication Tokens**

Just like you need a badge to access a secure building, you need a token to access different tools and data inside the Tapis platform. Tapis tokens are **digital keys** that prove your identity when you're using Tapis services.

When you log in to Tapis (using your username and password or other method), you get a **token**. This token is what tells Tapis, “I’m allowed to use these tools.”
The token is a long string with apparently-random characters. 

## Why Tokens?

Tapis is built to help researchers and developers run jobs, access data, manage systems, and more — often from different computers and applications. Tokens make this secure and flexible.

Tokens let Tapis:

* **Know who you are**
* **Check what you’re allowed to do**
* **Let you interact with the system without needing to send your password every time**

## How Tokens Work (Simplified)

1. **You log in**
   You use your credentials to log in through the Tapis authentication service (either directly or through a script or app).

2. **Tapis gives you a token**
   The system returns a token — a long string of letters and numbers — that represents **you** for a limited amount of time.

3. **You use the token in your requests**
   When you want to call a Tapis API (e.g., to run a job or access files), you include the token in the header of your request:

   ```
   Authorization: Bearer <your_token_here>
   ```

4. **Tapis checks the token**
   Behind the scenes, Tapis checks that the token is valid and sees what you’re allowed to do. If everything checks out, the action goes through.

5. **Tokens expire**
   Tokens are only valid for a short period (usually minutes). After that, you’ll need to log in again to get a new one.

## Save the Token

You can **save this token** to a file and use it until it expires. This way you don't have to enter your password as often.

Saving your token means:

* You **don’t need to log in again** every time you run a script (as long as the token hasn’t expired).
* You can **load it into other scripts** without exposing your username/password.

```{admonition} Tips for Beginners
* **Treat your token like a password** — never share it or post it publicly.
* **You don’t need to remember your token** — just copy and paste it when needed.
```

 -->