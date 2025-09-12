# David Chui's Self-Hosted Raspberry Pi Portfolio Cluster

[![GitLab CI/CD](https://img.shields.io/gitlab/pipeline-status/your-gitlab-username/your-repo-name?branch=main&style=for-the-badge&logo=gitlab)](https://gitlab.com/your-gitlab-username/your-repo-name/-/pipelines)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

This repository contains the complete infrastructure-as-code and application source for my personal portfolio, running on a distributed, 5-node Raspberry Pi cluster. This is a living project designed to showcase a deep, practical understanding of modern DevOps, cloud-native architecture, and full-stack development in a real-world, self-hosted environment.

---

### 🚀 **Live Project Links**

* **Static Resume Host:** **[resume.davidchui.work](https://resume.davidchui.work)**

---

### 🏛️ **Cluster Architecture**

The entire system is designed with a clear separation of concerns, utilizing a secure overlay network (Tailscale) for inter-node communication and isolating management services from the public-facing application.


*A high-level overview of the portfolio cluster architecture.*

### ✅ **Core Features**

* **Automated Deployments:** Push a commit to `main` and a GitLab CI/CD pipeline automatically builds, tests, and deploys the application containers.
* **Live Observability:** A real-time Grafana dashboard visualizes health metrics (CPU, RAM, temp) and logs from every node in the cluster.
* **Infrastructure as Code (IaC):** The entire cluster setup, from installing Docker to configuring networking, is automated and version-controlled with Ansible.
* **AI-Powered Chatbot:** An interactive "AMA" bot, trained on my personal history and served via a dedicated Python API, allows for a unique way to engage with my resume.
* **Secure Remote Access:** The entire cluster is accessible for management over a secure Tailscale (WireGuard) VPN, with no exposed SSH ports.
* **Self-Hosted Analytics:** A privacy-first Umami instance provides web analytics without relying on third-party services.

---

###  Raspberry Pi Cluster: Hardware & Roles

The cluster is comprised of five Raspberry Pis, each with a specialized role:

* 🔹 **Pi 0 (3B+ 512MB):** Serves as a dedicated, low-power resume host.
* 🔹 **Pi 1 (5 4GB):** The **Automation & Gateway Node**. It runs the GitLab CI/CD runner, a secure Tailscale VPN gateway, and an internal-only Caddy reverse proxy for management dashboards.
* 🔹 **Pi 2 (5 4GB):** The **Web & Observability Hub**. This hosts the primary portfolio website, its backend API, a public-facing reverse proxy, and the central Prometheus & Grafana monitoring services.
* 🔹 **Pi 3 (5 8GB):** The **Data Hub**. It runs a PostgreSQL database for logging visitor interactions and the self-hosted Umami analytics platform.
* 🔹 **Pi 4 (5 16GB):** The **AI Agent Host**. This powerhouse Pi is dedicated to hosting the custom-trained "AMA" (Ask Me Anything) chatbot.

---

### 🛠️ **Technology Stack**

This project utilizes a modern, cloud-native technology stack that is highly relevant in today's software engineering landscape.

| Category                  | Technologies                                                              |
| ------------------------- | ------------------------------------------------------------------------- |
| **DevOps & Automation** | `Ansible`, `Docker`, `Docker Compose`, `GitLab CI/CD`, `Git`                |
| **Networking & Security** | `Tailscale (WireGuard)`, `Caddy`, `Nginx Proxy Manager`, `Cloudflare`       |
| **Observability** | `Prometheus`, `Grafana`, `Loki`, `Promtail`, `Node Exporter`               |
| **Frontend & Web** | `React (Vite)`, `Node.js`, `Express`, `Tailwind CSS`                        |
| **AI & Backend** | `Python`, `FastAPI`, `PyTorch` / `Transformers`                           |
| **Data & Analytics** | `PostgreSQL`, `Umami`                                                     |
| **Operating System** | `Ubuntu Server 24.04 LTS` (on all Pi 5s)                                  |

---

### 📂 **Repository Structure**

This repository is structured to separate concerns, making it easy to manage and scale.
