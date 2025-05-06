After the **base image**, Docker builds your custom image layer by layer based on the instructions in your `Dockerfile`.

Here’s what typically comes **after the base image**:

---

### 🧱 Dockerfile Layer Breakdown (After `FROM`)

1. **`WORKDIR`** – Sets the working directory inside the container.

   ```dockerfile
   WORKDIR /app
   ```

2. **`COPY` / `ADD`** – Copies your app code and files into the container.

   ```dockerfile
   COPY . /app
   ```

3. **`RUN`** – Installs dependencies or runs setup commands.

   ```dockerfile
   RUN pip install -r requirements.txt
   ```

4. **`ENV`** – Sets environment variables.

   ```dockerfile
   ENV PYTHONUNBUFFERED=1
   ```

5. **`EXPOSE`** – Declares which port your app listens on (for documentation).

   ```dockerfile
   EXPOSE 8000
   ```

6. **`CMD`** or **`ENTRYPOINT`** – Defines the default command when the container starts.
   ```dockerfile
   CMD ["python", "app.py"]
   ```

---

### 🧠 Layer Concept

Each of these instructions creates a **new layer** on top of the base image. Docker caches layers, which speeds up rebuilds if earlier layers haven’t changed.

---

Would you like a commented sample Dockerfile showing these steps in action?
