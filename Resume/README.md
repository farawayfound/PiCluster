# 🌐 Interactive Resume on Raspberry Pi

This project hosts my interactive resume on a **Raspberry Pi 3 B+** as a self-contained, demo-ready static site.  
It demonstrates not only my professional journey but also my ability to design, harden, and operate reliable systems end-to-end — from hardware to frontend UX.

---

## 📖 Purpose

- Provide employers and collaborators a **living, interactive resume** beyond a static PDF.
- Showcase skills in **systems engineering, DevOps, security hardening, and frontend design**.
- Experiment with **self-hosting** on constrained hardware (Pi 3 B+ with 512 MB RAM) to highlight optimization and security practices.

---

## 🛠️ Underlying Hardware & Network

- **Raspberry Pi 3 B+** (512 MB RAM)  
- **32 GB A2 microSD card** (with optional usb boot from backup if card fails)  
- **120 mm PWM fan** for cooling (shared across my Pi cluster)  
- **Network:**  
  - No router port forwarding  
  - Secure ingress via **Cloudflare Tunnel**  
  - DNS + TLS termination handled by Cloudflare  
- **Power:** simple UPS to protect against corruption

---

## 🏗️ Software Stack

- **Web server:** [Caddy](https://caddyserver.com/) (lightweight, secure defaults, auto-headers)  
- **Tunnel:** [cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/) (no open ports required)  
- **Frontend:** HTML, CSS, vanilla JS (future expansion: Astro + Tailwind with React “islands”)  
- **Version control & CI/CD:** GitHub → deploy via `scp`/`rsync` or GitHub Actions to the Pi  
- **Monitoring:** Local health check (`/health.txt`), systemd logs, Cloudflare analytics  

---

## 🎯 Design Goals

- **Minimal footprint:** small static site runs comfortably on <1% of Pi resources.  
- **Security first:** no open ports; hardened SSH, UFW firewall, Fail2Ban, and Cloudflare WAF.  
- **Resilience:** static hosting eliminates runtime errors; simple restart recovers full service.  
- **Elegance:** clean design, animated timeline, PDF download, and lazy-loaded images.  
- **Extensibility:** built to scale into a broader **Pi cluster portfolio** (monitoring dashboards, AI demos, etc.).

---

## 📂 Project Structure

```text
/srv/resume/site
├── index.html                # Interactive resume
├── assets/                   # Images, headshot, logos, future projects
│   ├── headshots/
│   │   └── headshot.jpg
│   └── logos/
│       ├── hchb.jpg
│       ├── onetrust.jpg
│       └── usaf.jpg
├── data/                     # Centralized JSON configs
│   └── links.json
├── downloads/                # Resume PDFs and supporting docs
│   └── resumes/
│       └── Long-Form-Resume.pdf
└── health.txt                # Health endpoint for monitoring
```

---

## 🚀 Deployment Workflow

1. **Local dev** → edit `index.html`, assets, or JSON data.  
2. **Push to Pi** (manual):  
   ```powershell
   scp -r ./assets ./data ./downloads ./health.txt ./index.html \
       david@pi-resume:/srv/resume/site/
3. CI/CD option: GitHub Actions build + deploy via rsync using a deploy key.

4. Cloudflare Tunnel routes resume.davidchui.work → local Caddy on port 8080.

⚠️ Design Limitations
Runs on single low-power hardware (no redundancy).

Static assets only; no backend forms or databases.

Cached assets can occasionally surface stale 403s with Cloudflare — mitigated by cache purges or versioned URLs.

Built primarily to demonstrate engineering mindset, not replace a professional hosting service.

🌟 Future Enhancements
Switch to Astro + Tailwind for more maintainable component structure.

Add React islands for project galleries and filters.

CI/CD pipeline for automatic deploys on main branch push.

Integrate lightweight monitoring dashboard across my Pi cluster.

Optional: PWA support for offline resume access.

👤 About Me
David Chui

Technical Engineer II @ Hearst Health (HomeCare HomeBase)

Former USAF Structural Engineer

B.S. Finance & Information Systems (University of Colorado Denver, 2025)

Experienced in C#/.NET, Azure, SQL, Kubernetes, Python, and PowerShellLong Form ResumeLong Form Resume

📧 david.chui@outlook.com · LinkedIn · GitHub

📜 License
This project is personal and non-commercial. You’re welcome to fork for learning purposes, but please do not redistribute the resume content as your own.

---

Would you like me to also draft a **shorter, recruiter-facing version** (like a polished project description you could paste on your LinkedIn portfolio), or should we keep this just as a GitHub README?





Ask ChatGPT


