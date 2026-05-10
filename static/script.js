const glow = document.querySelector(".cursor-glow");
const neuralCanvas = document.querySelector("#neuralCanvas");
const chatForm = document.querySelector("#chatForm");
const chatInput = document.querySelector("#chatInput");
const chatMessages = document.querySelector("#chatMessages");
const mobileToggle = document.querySelector("#mobileToggle");
const primaryNav = document.querySelector("#primaryNav");
const promptButtons = document.querySelectorAll("[data-question]");
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

function startNeuralCanvas() {
  if (!neuralCanvas || reduceMotion) return;

  const context = neuralCanvas.getContext("2d");
  const points = [];
  let width = 0;
  let height = 0;
  let animationFrame = 0;

  function resize() {
    const pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;
    neuralCanvas.width = width * pixelRatio;
    neuralCanvas.height = height * pixelRatio;
    neuralCanvas.style.width = `${width}px`;
    neuralCanvas.style.height = `${height}px`;
    context.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);

    points.length = 0;
    const total = Math.min(72, Math.floor((width * height) / 18000));
    for (let index = 0; index < total; index += 1) {
      points.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.35,
        vy: (Math.random() - 0.5) * 0.35,
      });
    }
  }

  function draw() {
    context.clearRect(0, 0, width, height);

    for (const point of points) {
      point.x += point.vx;
      point.y += point.vy;

      if (point.x < 0 || point.x > width) point.vx *= -1;
      if (point.y < 0 || point.y > height) point.vy *= -1;
    }

    for (let i = 0; i < points.length; i += 1) {
      for (let j = i + 1; j < points.length; j += 1) {
        const first = points[i];
        const second = points[j];
        const distance = Math.hypot(first.x - second.x, first.y - second.y);

        if (distance < 150) {
          const opacity = (1 - distance / 150) * 0.18;
          context.strokeStyle = `rgba(215, 255, 57, ${opacity})`;
          context.lineWidth = 1;
          context.beginPath();
          context.moveTo(first.x, first.y);
          context.lineTo(second.x, second.y);
          context.stroke();
        }
      }
    }

    for (const point of points) {
      context.fillStyle = "rgba(112, 214, 255, 0.62)";
      context.beginPath();
      context.arc(point.x, point.y, 1.6, 0, Math.PI * 2);
      context.fill();
    }

    animationFrame = requestAnimationFrame(draw);
  }

  resize();
  draw();
  window.addEventListener("resize", resize);
  window.addEventListener("beforeunload", () => cancelAnimationFrame(animationFrame));
}

window.addEventListener("pointermove", (event) => {
  if (!glow) return;
  glow.style.left = `${event.clientX}px`;
  glow.style.top = `${event.clientY}px`;
});

startNeuralCanvas();

mobileToggle?.addEventListener("click", () => {
  const isOpen = mobileToggle.getAttribute("aria-expanded") === "true";
  mobileToggle.setAttribute("aria-expanded", String(!isOpen));
  primaryNav?.classList.toggle("open", !isOpen);
});

primaryNav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    mobileToggle?.setAttribute("aria-expanded", "false");
    primaryNav?.classList.remove("open");
  });
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  },
  { threshold: 0.14 }
);

document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));

function addMessage(role, text) {
  const message = document.createElement("div");
  message.className = `message ${role}`;
  message.textContent = text;
  chatMessages.appendChild(message);
  chatMessages.scrollTop = chatMessages.scrollHeight;
  return message;
}

function typeMessage(element, text) {
  if (reduceMotion || text.length > 1800) {
    element.textContent = text;
    return;
  }

  element.textContent = "";
  let index = 0;
  const step = () => {
    element.textContent += text.slice(index, index + 3);
    index += 3;
    chatMessages.scrollTop = chatMessages.scrollHeight;
    if (index < text.length) {
      window.setTimeout(step, 10);
    }
  };
  step();
}

promptButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const question = button.dataset.question;
    if (!question || !chatInput) return;

    document.querySelector("#assistant")?.scrollIntoView({ behavior: "smooth", block: "start" });
    chatInput.value = question;
    window.setTimeout(() => chatInput.focus(), 420);
  });
});

chatForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const question = chatInput.value.trim();
  if (!question) return;

  addMessage("user", question);
  chatInput.value = "";
  chatInput.disabled = true;
  chatForm.querySelector("button").disabled = true;

  const loadingMessage = addMessage("bot loading", "Thinking through Om's personal data...");

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    if (!response.ok) {
      throw new Error("Request failed");
    }

    const data = await response.json();
    loadingMessage.className = "message bot";
    typeMessage(loadingMessage, data.answer);
  } catch (error) {
    loadingMessage.className = "message bot";
    loadingMessage.textContent = "I could not reach the chatbot backend. Please try again after restarting the server.";
  } finally {
    chatInput.disabled = false;
    chatForm.querySelector("button").disabled = false;
    chatInput.focus();
  }
});
