---
title: Project Continuum Product Proposal
document_id: continuum-product-proposal
version: 0.3
status: active
owner: Product Owner
last_updated: 2026-07-21
supersedes: 0.2
confidentiality: confidential-working-draft
authoritative_format: markdown
export_reference: docs/reference/exports/project-continuum-proposal-v0.3.docx
---

# Project Continuum

## The Next-Generation Human-AI Relationship Platform

A proposal for a persistent digital partner that earns trust, builds relational continuity, and coordinates the best available intelligence on the user's behalf.

| Relationship | Intelligence | Autonomy |
|---|---|---|
| Persistent identity and emotional continuity | Multi-model reasoning and skills | Task-specific trust earned through outcomes |

> **Document authority**
>
> This Markdown document is the canonical strategic proposal. DOCX and PDF copies are presentation exports. When an export conflicts with this file, this file and its Git history are authoritative.

*Working title only. The consumer name has not been trademark or domain screened.*

Prepared as a product strategy and MVP execution proposal. Version 0.3 - July 21, 2026.

## Executive summary

### From AI tool to trusted digital partner

Today’s AI products are improving rapidly, but most still organize the experience around a model, an app, or a task. They may remember user information, execute scheduled work, or simulate companionship, yet the relationship remains fragmented across providers and channels. Users repeatedly rebuild context, manually initiate most interactions, and choose between productivity agents that lack relational depth and companion agents that lack accountable real-world capability.

Project Continuum proposes a different product category: a persistent, model-independent digital partner. It develops both operational trust and relational trust; communicates through the channels users already inhabit; uses multiple reasoning providers as interchangeable consultants; stores identity and memory outside any single model; and earns task-specific autonomy through demonstrated outcomes.

> **North-star product definition**
>
> A persistent digital partner that knows the user over time, communicates naturally through text and voice, initiates meaningful interactions at appropriate moments, coordinates multiple AI models and tools, and earns the right to act independently one responsibility at a time.

### The MVP must test the relationship, not the full dream

The first release should not attempt to build an always-on life operating system, humanoid avatar, skill marketplace, proprietary model, or dedicated hardware. It should prove three things with a narrow but coherent experience:

1. Users voluntarily build shared context with the agent because continuity is useful and emotionally meaningful.

2. Agent-initiated interactions are welcomed when they are relevant, well-timed, and easy to control.

3. Users progressively delegate more responsibility after seeing evidence that the agent performs reliably.

### Recommended MVP shape

A Telegram-first founder alpha delivered as a private one-to-one bot conversation, supported by a minimal owned control center for memory, trust, diagnostics, cost, and account settings. Telegram is the first user interface, not the system of record. The backend remains channel-independent so additional messaging platforms, a native application, desktop presence, and real-time calling can be added through adapters without changing the persistent agent identity or relationship state.

### Contents

1. [What's the challenge today](#1-whats-the-challenge-today)
2. [Our vision for solving the challenge](#2-our-vision-for-solving-the-challenge)
3. [The user experience](#3-the-user-experience)
4. [Key product features](#4-key-product-features)
5. [Market landscape and differentiation](#5-market-landscape-and-differentiation)
6. [High-level solution architecture](#6-high-level-solution-architecture)
7. [Business model](#7-business-model)
8. [MVP definition](#8-mvp-definition)
9. [Backlog post MVP](#9-backlog-post-mvp)
10. [Project plan](#10-project-plan)
11. [Development and maintenance process](#11-development-and-maintenance-process)
12. [Appendix: Market references and proposal notes](#appendix-market-references-and-proposal-notes)

## 1. What's the challenge today

The market has powerful AI capabilities, but no coherent relationship layer that compounds trust and value over time.

### AI is still organized around transactions

The dominant interaction remains: open an application, formulate a prompt, receive an answer, and leave. Even when a product remembers details or performs scheduled work, the user generally remains responsible for initiating the relationship, selecting the right model, reconstructing context, and supervising the workflow.

| **Challenge**                                | **Why it matters**                                                                                                                                                                                |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Reactive by default**                      | Most systems wait for prompts. Scheduled tasks and notifications exist, but they are typically user-programmed automations rather than socially aware, context-sensitive initiative.              |
| **Fragmented identity**                      | The user has separate histories and relationships with ChatGPT, Claude, Gemini, companion apps, messaging bots, and specialized agents. None is the durable identity above the models.            |
| **Vendor-locked memory**                     | Personal context is usually stored inside a provider’s product. Switching models can mean losing accumulated relationship value or performing awkward exports and imports.                        |
| **Trust is binary or permission-based**      | Current systems focus on whether a tool has access, not whether the agent has earned confidence for a specific responsibility through a history of outcomes.                                      |
| **Productivity and companionship are split** | General assistants optimize work but often feel transactional. Companion products create emotional engagement but are not designed for accountable multi-step execution across the user’s life.   |
| **Proactivity can become spam**              | Notifications are easy to implement; good judgment about when to engage is hard. Poor timing rapidly destroys trust and retention.                                                                |
| **The model is mistaken for the agent**      | When identity, memory, behavior, and intelligence are fused to one LLM, the product becomes vulnerable to provider changes, model regressions, cost shifts, and commoditization.                  |
| **Emotional design carries real risk**       | A relationship product can drift into flattery, dependency, simulated affection for payment, or displacement of human relationships unless incentives and safeguards are designed from the start. |

> **Core opportunity**
>
> Create the missing relationship layer above models, tools, channels, and tasks - a layer that maintains identity, memory, trust, social judgment, and accountability as the underlying technology changes.

### The user’s unmet need

Users do not merely need more answers. They need continuity and intelligent attention: someone that understands what matters, remembers unresolved commitments, notices patterns, challenges weak thinking, helps with emotional and practical needs, and can increasingly carry work without requiring a new setup every time.

The hard problem is therefore not “build a chatbot with memory.” It is:

> **Design challenge**
>
> How can an AI become useful enough to earn responsibility, consistent enough to earn trust, and emotionally intelligent enough to become part of everyday life - without pretending to be human or manipulating the user?

## 2. Our vision for solving the challenge

A model-independent digital partner that develops a durable relationship and earns autonomy one responsibility at a time.

### Vision statement

We are designing the next-generation blueprint for human-AI relationships: moving AI from a reactive tool into a trusted, evolving digital partner.

### The product has two forms of trust

| **Trust dimension**   | **Question**                                                                                                          | **How it is earned**                                                                                                        |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Operational trust** | Can the agent perform this responsibility correctly, safely, and consistently?                                        | Evidence from task outcomes, user approval, reversals, errors, cost, and timeliness.                                        |
| **Relational trust**  | Can the user be honest with the agent, rely on its discretion, and expect consistent, appropriate behavior over time? | Evidence from memory accuracy, privacy behavior, emotional appropriateness, constructive disagreement, and conflict repair. |

### Foundational principles

- **The relationship is the product.** Models, apps, and tools are replaceable components. The persistent identity and accumulated relationship are the durable asset.

- **Autonomy is earned, not enabled.** Every responsibility begins with observation or recommendation. Authority increases only after demonstrated performance and explicit or conversational user consent.

- **Trust belongs to work, not the whole agent.** A user may authorize autonomous calendar cleanup while requiring approval for emails and prohibiting financial actions.

- **Memory belongs to the user.** Identity, preferences, relationship history, skills, and trust records are maintained outside the LLM, inspectable and portable.

- **Proactivity requires social judgment.** The agent must decide whether an observation is important, reliable, timely, and worth interrupting the user for.

- **Emotional intelligence without emotional deception.** The agent may recognize feelings and respond with warmth, but it must not falsely claim human consciousness or sell affection.

- **One partner, many intelligences.** The agent can consult different models, tools, and specialized agents while preserving one accountable voice and identity.

- **Learning must change behavior.** Storing facts is not learning. The system must improve decisions, timing, procedures, and model selection based on outcomes and feedback.

### The relationship loop

| Step | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Loop | Observe | Understand | Engage | Act | Evaluate | Learn | Earn trust |

### What the product is not

- Not a thin wrapper that forwards every message to one LLM.

- Not an automation builder that requires users to define flows before value appears.

- Not a simulated romantic relationship optimized for session length.

- Not a fully autonomous agent that begins with broad access to the user’s accounts.

- Not a proprietary foundation-model company in the initial business plan.

## 3. The user experience

A persistent contact in the user’s life, supported by an owned control center and available across channels.

### Primary interaction metaphor: a person, not an application

The agent should be reachable like another trusted contact. The first implementation will appear as a Telegram bot in a private chat. The user can send text, voice notes, images, videos, and files; after the user has started the conversation, the agent can send relevant follow-ups and proactive messages subject to quiet hours and interruption controls. Telegram is the first conversation surface, while identity, memory, trust, reasoning, learning, and action remain in the owned backend.

> **Channel strategy**
>
> Messaging-first, but channel-independent. Third-party platforms are convenient front doors; the agent’s identity, memory, policy, and history remain in the Continuum platform.

### Initial channel decision: Telegram-first

Telegram is recommended for the first personal build because its Bot API is an HTTP-based developer interface, supports webhooks, rich media, Mini Apps, notifications, and bot monetization, and is free for normal bot use. The choice is tactical rather than permanent: Telegram supplies the conversation shell while Continuum owns the relationship and intelligence layers. [9] [10] [11]

| **Decision area**           | **Founder-alpha approach**                                                                                                               | **Constraint or implication**                                                                                                            |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Identity and onboarding** | Create a clearly labeled bot through BotFather; use a private-chat deep link and a short transparent introduction.                       | A bot is visibly identified as a bot. The user must message or start it before it can continue the conversation.                         |
| **Inbound communication**   | Receive Telegram Update objects over an authenticated HTTPS webhook; support text and voice notes first, then files and media.           | Webhook handling must be idempotent because updates may be retried or arrive out of order.                                               |
| **Proactive communication** | Store the authorized chat ID after onboarding and send low-frequency check-ins through an outbound queue.                                | Respect quiet hours, user controls, per-chat rate limits, retry_after, and anti-spam expectations.                                       |
| **Real-time calls**         | Defer live voice/video calls; use asynchronous voice notes for the founder alpha.                                                        | The Bot API currently has no native bot call interface. A later calling adapter must preserve the same identity and memory.              |
| **Privacy boundary**        | Treat Telegram as a transport and minimize sensitive content placed in messages; maintain durable memory in the owned encrypted backend. | Cloud bot chats are not Telegram Secret Chats. The product must disclose the boundary and provide deletion and private-session controls. |
| **Platform resilience**     | Keep every Telegram identifier mapped to an internal user and agent ID through the channel adapter.                                      | No business logic, memory schema, or trust policy may depend directly on Telegram-specific objects.                                      |

### Experience surfaces

| **Surface**                          | **Experience**                                                                                                                                         | **Role in strategy**                                                                                   |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| **Telegram private bot chat**        | Primary founder-alpha interface for text, voice notes, images, video, files, buttons, and controlled proactive messages after the user starts the bot. | Fastest route to a contact-like experience using an existing mobile and desktop application.           |
| **Minimal owned control center**     | Memory inspection and correction, trust and permission settings, connected services, audit history, usage/cost, privacy controls, and diagnostics.     | Keeps the agent portable and governable without forcing the first conversation into a new application. |
| **Developer and operations console** | Webhook status, queues, model calls, traces, tests, incidents, replay, and feature flags.                                                              | Essential for building safely with coding agents and for debugging relationship behavior.              |
| **Future channel adapters**          | Slack, Microsoft Teams, WhatsApp, WeChat, Instagram, SMS/RCS, owned mobile/desktop apps, voice calling, wearables, car, and hardware.                  | Added through the same canonical message contract after the Telegram experience is stable.             |

### Conversational onboarding

Avoid a long setup wizard. The agent begins with a transparent introduction, asks a small number of high-value questions, and learns the rest through interaction.

1. Choose the agent’s name, baseline demeanor, voice, and preferred channels.

2. Explain what the agent can observe, remember, and do - in plain language.

3. Ask what kind of relationship the user wants: practical assistant, thinking partner, coach, companion, or a blend.

4. Agree on initial communication boundaries: quiet hours, proactive frequency, sensitive topics, and approval requirements.

5. Begin with zero autonomous authority and a small set of suggested routines.

### A day in the experience

| **Moment**                | **What the experience should feel like**                                                                                                                                       |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Morning**               | The agent sends a short, context-aware greeting and highlights two or three meaningful items. It asks about the user’s energy or priorities rather than dumping a dashboard.   |
| **During work**           | The user messages naturally. The agent reasons, researches, drafts, or proposes an action. When it lacks capability, it explains the gap instead of pretending.                |
| **A free window appears** | The agent may suggest a useful activity based on goals, unfinished commitments, and current energy - but only if confidence and timing exceed the user’s engagement threshold. |
| **Delegated work**        | The agent performs approved steps, reports exceptions, and returns with outcomes rather than a stream of internal status noise.                                                |
| **Evening**               | It may reflect on the day, celebrate progress, revisit something emotionally important, or stay quiet. The objective is relevance, not forced engagement.                      |
| **After mistakes**        | The agent names what happened, asks for the minimum useful feedback, updates its procedure or trust level, and shows the change.                                               |

### How proactivity should work

Proactivity is a decision, not a notification rule. Before initiating, the agent evaluates:

- Importance and urgency

- Confidence in the observation

- User availability and current context

- Recency and frequency of prior interruptions

- Expected value versus disruption

- Preferred tone and channel

- Whether action can wait for the next natural conversation

Every proactive message should support “not now,” “less often,” “never for this,” and “this was useful” as natural conversational feedback. These signals become training data for timing and relevance.

### Text, voice, and video

Text and voice notes belong in the first build because Telegram bots support rich messaging and media exchange. The current Bot API does not provide native user-to-bot voice or video calling, so real-time calls should be introduced later through another supported channel or a dedicated calling service. Video files and video notes may be exchanged in Telegram, but a live video avatar is not required to validate the relationship model. [9] [10] [11]

## 4. Key product features

The relationship engine combines identity, memory, social judgment, intelligence orchestration, action, and evidence-based trust.

| **Feature**                         | **Description**                                                                                                                                                                               | **Target**         |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| **Persistent agent identity**       | One consistent partner across channels and model providers; stable principles with an adapting communication style.                                                                           | MVP                |
| **External user-controlled memory** | Personal, relational, episodic, semantic, procedural, outcome, and trust memories; inspect, correct, delete, and export.                                                                      | MVP                |
| **Dual trust system**               | Operational trust per responsibility plus relational trust signals; authority can increase, decrease, or expire.                                                                              | MVP                |
| **Proactive engagement engine**     | Context-aware initiation with interruption budgets, quiet hours, confidence thresholds, and user feedback.                                                                                    | MVP                |
| **Multi-model reasoning router**    | Select model by task, quality, latency, cost, privacy, and user preference; support critique or consensus for important decisions.                                                            | MVP                |
| **Planning and task execution**     | Break goals into steps, request approvals, use connected tools, manage exceptions, and report outcomes.                                                                                       | MVP - limited      |
| **Relationship intelligence**       | Recognize emotional context, shared history, conversational rhythm, disagreement, and repair without pretending to have human feelings.                                                       | MVP - basic        |
| **Learning and evaluation**         | Capture outcomes and feedback; update memory, procedures, routing, and trust.                                                                                                                 | MVP                |
| **Capability acquisition**          | Recognize missing skills, propose a safe learning path, test, and register the new capability.                                                                                                | Post-MVP           |
| **Cross-channel continuity**        | Maintain one conversation and relationship across app, messaging, desktop, calls, and devices.                                                                                                | MVP - two surfaces |
| **Agent-to-agent consultation**     | Consult external models or specialized agents as tools while the primary agent remains accountable.                                                                                           | MVP - model APIs   |
| **Developer and skill ecosystem**   | Third-party tools, skills, evaluation packs, memory modules, and communication integrations.                                                                                                  | Post-MVP           |
| **Channel adapter framework**       | Platform-specific adapters translate Telegram, Slack, Teams, and future channel events into one canonical interaction envelope and translate responses back to each platform.                 | MVP - Telegram     |
| **Engineering harness**             | Requirement-to-code workflow with architecture rules, contract tests, synthetic conversations, model evaluations, staging bot, deployment gates, rollback, and machine-readable test reports. | MVP                |

### Trust state for each responsibility

| **State**                 | **Authority**                                                                                                        |
|---------------------------|----------------------------------------------------------------------------------------------------------------------|
| **Observe**               | May use authorized data to understand context. Cannot recommend or act beyond the conversation.                      |
| **Recommend**             | May propose actions and explain reasoning. User performs the action.                                                 |
| **Prepare**               | May draft or stage the action. User reviews and approves execution.                                                  |
| **Execute with approval** | May execute after an explicit confirmation each time.                                                                |
| **Execute within limits** | May act autonomously inside agreed constraints and report afterward.                                                 |
| **Manage by exception**   | May own the responsibility and involve the user only when policy, uncertainty, cost, or risk thresholds are crossed. |

The trust state is never only a static setting. It is informed by outcomes, recency, task risk, model confidence, and the user’s expressed preference. High-risk domains may remain permanently approval-gated.

### Memory model

| **Memory type** | **Purpose**                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------|
| **Personal**    | Stable facts, preferences, values, goals, communication preferences.                        |
| **Relational**  | Shared history, meaningful moments, unresolved tensions, agreements, and inside references. |
| **Episodic**    | What happened in a specific conversation, event, or task.                                   |
| **Semantic**    | Generalized understanding derived from multiple experiences.                                |
| **Procedural**  | How the user wants recurring work performed.                                                |
| **Outcome**     | What succeeded, failed, cost more than expected, or created unintended consequences.        |
| **Trust**       | Authority, evidence, exceptions, and confidence for each responsibility.                    |

### Product safety and integrity requirements

- **No paid affection.** Payment cannot unlock greater warmth, loyalty, emotional validation, or exclusivity.

- **No false human claims.** The agent may have personality and continuity but must not assert biological feelings or consciousness as fact.

- **No silent authority expansion.** The agent cannot increase its own permissions merely because prior work succeeded.

- **No hidden memory.** The user can inspect material memories and understand why they influenced important behavior.

- **No engagement-at-all-costs optimization.** Success metrics must include usefulness, trust, and user well-being rather than time spent alone.

- **Escalation for vulnerable situations.** The experience needs crisis, abuse, self-harm, and dependency safeguards designed with qualified experts.

## 5. Market landscape and differentiation

Existing products prove demand for memory, proactivity, voice, and companionship - but the full relationship architecture remains fragmented.

Market snapshot as of July 19, 2026. The comparison uses public product documentation and should be refreshed before fundraising or external publication.

| **Offering**                   | **Category**                               | **Relevant strengths**                                                                                                                                        | **Gap relative to Continuum**                                                                                                                                                    |
|--------------------------------|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ChatGPT**                    | General AI assistant                       | Automatically synthesized memory from chats, files, and connected apps; editable memory summary; scheduled and monitoring tasks with notifications.[1][2] | The relationship remains centered on the ChatGPT product and OpenAI model ecosystem; trust is not presented as an evidence-based per-responsibility progression.                 |
| **Claude**                     | General AI assistant / work agent          | Account-wide instructions, project instructions, styles, and reusable skills for specialized behavior.[3]                                                   | Strong personalization and work capability, but not positioned as a persistent cross-channel relationship with proactive social judgment and task-specific trust.                |
| **Gemini**                     | General AI assistant / ecosystem assistant | Scheduled actions and deep integration with Google services; growing personalization and voice experiences.[4]                                              | Powerful ecosystem distribution, but identity and memory are tied to Google’s assistant layer rather than a user-portable multi-model relationship.                              |
| **Replika**                    | AI companion                               | Emotionally oriented relationship, personality, memory, customization, and calls; positioned as an AI friend that participates in everyday life.[5]         | Strong relational experience, but not primarily designed as a model-independent, accountable execution partner with transparent task trust and enterprise-grade action controls. |
| **Character.AI**               | Character / entertainment companion        | Custom characters, diverse voices, two-way voice calls, and switching between text and voice.[6]                                                            | Immersive and expressive, but characters are not a durable personal operating layer coordinating real-world work, memory portability, and responsibility-based autonomy.         |
| **Specialized agent products** | Automation / vertical agents               | Strong execution in defined domains such as research, scheduling, sales, coding, or browser tasks.                                                            | Typically task-first rather than relationship-first; the user assembles multiple agents without one persistent identity and trust system above them.                             |

### Differentiation thesis

No single reviewed offering publicly presents the following combination as one consumer product. Individual components will be copied; the defensible proposition is their integration into a coherent relationship system.

| **Differentiator**                             | **Why it is harder to replicate well**                                                                                                  |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Persistent relationship layer above models** | One identity and relationship can survive provider, model, channel, and device changes.                                                 |
| **Evidence-based, task-specific trust**        | The product records outcomes and evolves authority for each responsibility rather than applying blanket autonomy.                       |
| **Operational plus relational value**          | It aims to help with work and life while building shared context, emotional appropriateness, and continuity.                            |
| **Contextual proactivity**                     | The agent decides whether and when to engage rather than merely running scheduled prompts.                                              |
| **User-owned memory architecture**             | Personal and relationship memory is externalized, inspectable, portable, and not owned by the reasoning provider.                       |
| **Accountable intelligence brokerage**         | The agent can consult OpenAI, Anthropic, Google, local models, or specialized agents, but remains accountable for synthesis and action. |
| **Learning from outcomes**                     | Procedures, timing, routing, and trust change based on observed results, not only conversational preferences.                           |
| **Messaging-native presence**                  | The partner can appear as a contact in existing communication habits while maintaining an owned control plane.                          |

> **Critical competitive reality**
>
> Large AI platforms can reproduce most individual features. The venture only becomes defensible if relationship continuity creates compounding value: better timing, better procedures, richer shared history, stronger evaluation data, and higher earned responsibility.

## 6. High-level solution architecture

A channel-independent agent core separates relationship state from models, tools, and external platforms.

### Architecture overview

| Layer | Components |
|---|---|
| **Experience channels** | Telegram bot (first); minimal owned control center; developer console; future Slack, Teams, WhatsApp, WeChat, owned app, calls, and devices |
| **Channel and interaction gateway** | Telegram adapter; webhook verification; canonical interaction envelope; user/channel mapping; media normalization; outbound queue; rate limits; consent and delivery policy |
| **Relationship and agent core** | Persistent identity; conversation orchestrator; social judgment; goals; planning; proactivity; trust policy; approvals; channel-independent response |
| **Intelligence orchestration** | Provider adapters; model router; prompt/context assembly; reasoning modes; multi-model critique; cost, latency, and privacy policy; response synthesis |
| **Skills and actions** | Capability registry; action executor; calendar; communications; research; tasks; connected apps; sandbox; specialized agents; future marketplace |
| **Memory, learning, and governance** | Event store; typed memory; procedures; outcome store; evaluation; learning proposals; trust ledger; audit log; privacy and retention controls |
| **External providers** | Telegram Bot API; OpenAI API; Anthropic API; Gemini API; local/open models; speech services; user-connected applications |

### Core services

| **Service**                                 | **Responsibility**                                                                                                                                                              |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Identity service**                        | Defines stable values, boundaries, style, voice, and channel-independent continuity.                                                                                            |
| **Perception/context service**              | Transforms messages, calendar events, connected data, and device signals into structured context with provenance.                                                               |
| **Relationship manager**                    | Maintains shared history, emotional context, conversational rhythm, goals, and unresolved topics.                                                                               |
| **Proactivity engine**                      | Scores candidate interventions using value, urgency, confidence, timing, interruption budget, and channel policy.                                                               |
| **Planner/orchestrator**                    | Chooses reasoning modes, decomposes goals, identifies dependencies, and manages ongoing work.                                                                                   |
| **Model router**                            | Selects providers based on capability, cost, latency, privacy, availability, and user/provider preferences.                                                                     |
| **Trust policy engine**                     | Determines whether the agent may observe, recommend, prepare, execute with approval, execute within limits, or manage by exception.                                             |
| **Memory service**                          | Stores typed memories with source, confidence, sensitivity, retention, and user-control metadata.                                                                               |
| **Evaluation service**                      | Measures outcome quality, user corrections, reversals, timing, cost, and safety events.                                                                                         |
| **Audit and governance service**            | Produces an explainable record of data accessed, models consulted, actions proposed, approvals, execution, and memory updates.                                                  |
| **Channel adapter registry**                | Implements a stable adapter contract for inbound events, outbound messages, capabilities, delivery receipts, errors, and platform-specific policy.                              |
| **Interaction gateway and event bus**       | Authenticates channel events, maps external identities to internal users, creates the canonical interaction envelope, deduplicates events, and distributes work asynchronously. |
| **Capability registry and action executor** | Describes available skills, required permissions, inputs, outputs, risks, tests, and execution status; runs actions only under trust-policy decisions.                          |
| **Learning service**                        | Converts corrections, evaluations, and outcomes into proposed memory, procedure, routing, prompt, and capability changes with versioning and rollback.                          |

### Scaffold-first implementation strategy

Build every major boundary at the beginning, but do not build every capability deeply. The first milestone is a real end-to-end walking skeleton: Telegram input reaches the owned backend, passes through stable interfaces, and returns a response. A scaffold is not throwaway code; it is a versioned contract with a test double, observability, and a clear replacement path. This reduces future structural rewrites without pretending that placeholder logic is production intelligence.

| **Component scaffold**               | **Initial implementation**                                                                  | **First meaningful enrichment**                                                                                       |
|--------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Telegram channel adapter**         | Webhook receiver, message sender, identity mapping, error normalization, and test fixtures. | Voice-note/media handling, proactive queue, delivery receipts, Mini App links, and production rate limiting.          |
| **Interaction gateway / perception** | Canonical interaction envelope and deterministic intent/content classifier.                 | Multimodal normalization, provenance, sensitivity classification, and richer context extraction.                      |
| **Conversation orchestrator**        | Fixed pipeline that calls every component interface and returns a safe fallback.            | Dynamic routing among conversation, advice, planning, action, reflection, and learning paths.                         |
| **Identity and relationship**        | Static agent identity file plus user profile and conversation state.                        | Adaptive style, shared rituals, unresolved topics, emotional context, and relationship continuity.                    |
| **Memory**                           | Append-only conversation event store and a simple explicit fact store.                      | Typed episodic, semantic, procedural, outcome, and trust memory with retrieval, correction, deletion, and provenance. |
| **Reasoning and model providers**    | One provider adapter and one basic response policy.                                         | Model routing, reasoning modes, second opinions, cost/privacy policy, and evaluated synthesis.                        |
| **Trust and policy**                 | Deny-by-default action gate; every external action requires explicit approval.              | Responsibility-specific trust states, risk classification, limits, expiry, evidence, and exception management.        |
| **Proactivity**                      | Manual or scheduled test trigger that sends one approved check-in.                          | Candidate generation, timing score, interruption budget, quiet hours, feedback, and event-driven triggers.            |
| **Evaluation and learning**          | Conversation replay, thumbs/correction capture, and structured outcome event.               | Automated evaluations, procedure updates, memory proposals, regression checks, versioning, and rollback.              |
| **Skills and actions**               | Registry with dummy capabilities and a simulated action executor.                           | One real low-risk skill, then calendar/research/drafting, sandbox testing, and task-specific trust.                   |
| **Observability and governance**     | Structured logs, traces, cost records, audit events, feature flags, and health checks.      | Dashboards, incident replay, privacy reports, safety evaluation, and user-facing explanations.                        |

### Recommended component-deepening sequence

| **Order** | **Component to deepen**                                            | **Why this comes next**                                                                                | **Exit evidence**                                                                                            |
|-----------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **0**     | Contracts, repository rules, test harness, and all component stubs | Prevents the coding agent from collapsing the design into Telegram-specific or single-model code.      | Every service has a typed interface, owner, test double, telemetry event, and architecture test.             |
| **1**     | Telegram adapter and end-to-end communication loop                 | Creates visible value and proves deployment, networking, authentication, queues, and reply delivery.   | A private text message reliably produces a traced response in staging and production.                        |
| **2**     | Event store, observability, replay, and failure handling           | Without evidence and replay, later memory and learning behavior cannot be trusted or debugged.         | Every interaction can be reconstructed; duplicate updates and provider failures are handled safely.          |
| **3**     | Identity, conversation state, and basic relationship continuity    | The product must feel like the same partner before it tries to remember or act.                        | The agent maintains stable voice, user mapping, topic state, and transparent onboarding across sessions.     |
| **4**     | External memory                                                    | Memory is the first compounding asset and must be independent of the model provider.                   | The user can teach, retrieve, inspect, correct, delete, and suppress memories with provenance.               |
| **5**     | Reasoning and provider abstraction                                 | After context is reliable, improve how the agent thinks without binding the relationship to one model. | At least two model adapters pass the same contract tests; switching providers preserves identity and memory. |
| **6**     | Trust and approval policy                                          | No real-world action or autonomy should be introduced before deny-by-default governance exists.        | A simulated and one low-risk real action move through propose, approve, execute, audit, and rollback.        |
| **7**     | Proactivity                                                        | The agent can now use identity, memory, reasoning, and policy to initiate without becoming spam.       | One morning check-in and one event-driven follow-up are useful, controllable, and fully traced.              |
| **8**     | Evaluation and learning                                            | Behavior should only adapt after the system can measure outcomes and prevent regressions.              | Feedback produces reviewable change proposals; evaluated improvements can be promoted or rolled back.        |
| **9**     | Skills and bounded action expansion                                | New capabilities are safest after the learning and trust loops are observable.                         | Each new skill has a manifest, permissions, tests, risk level, evaluation criteria, and initial trust state. |

### Illustrative request flow

| **Step** | **Flow**                                                                                                                                                                                                                                     |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1**    | A user sends text, a voice note, media, or a command to the Telegram bot.                                                                                                                                                                    |
| **2**    | Telegram creates an Update object and sends an HTTPS POST to the registered webhook. The adapter verifies the secret header, records update_id, and rejects duplicates.                                                                      |
| **3**    | The Telegram adapter downloads or references media as needed and translates platform fields into a canonical interaction envelope containing internal user, agent, channel, conversation, content, timestamps, permissions, and provenance.  |
| **4**    | The interaction gateway persists the event, maps the Telegram chat to the internal relationship, and hands the envelope to the conversation orchestrator.                                                                                    |
| **5**    | The orchestrator invokes identity, relevant memory, reasoning, trust, proactivity, skills, and learning interfaces. During the first scaffold, some interfaces return deterministic placeholders while the end-to-end contract remains real. |
| **6**    | The model/provider layer generates a candidate response. Trust and policy determine whether the response is conversational, requests approval, or invokes an allowed action.                                                                 |
| **7**    | A channel-independent response object is created and passed to the Telegram adapter, which selects sendMessage, sendVoice, sendPhoto, sendDocument, or another appropriate Bot API method.                                                   |
| **8**    | The outbound queue delivers the response, respects Telegram limits, retries transient failures using retry_after, and records the delivery result.                                                                                           |
| **9**    | The event store, audit trail, evaluation service, and cost telemetry record what happened; later feedback may update memory, procedures, model routing, or a proposed trust level.                                                           |

### Data and privacy design

- Encrypt personal and relationship data in transit and at rest; isolate tenants and sensitive memory categories.

- Attach provenance, confidence, sensitivity, retention, and permitted-use metadata to each material memory.

- Minimize context shared with external models; send only what is necessary for the current purpose.

- Support temporary/private conversations that do not update long-term memory.

- Provide export, deletion, correction, and provider-disconnection controls.

- Treat retrieved content and memory as potentially untrusted input; apply prompt-injection defenses and provenance-aware policies.

- Require stronger approvals and auditability for money, reputation, health, legal, security, or irreversible actions.

### Hybrid model-provider design

The platform should fund default model access for a simple consumer experience while supporting user-connected developer accounts or local models for advanced users. Consumer subscriptions such as ChatGPT Plus do not include reusable API usage; OpenAI bills API usage separately, and Anthropic similarly requires a Claude Console account with separate billing.[7][8]

## 7. Business model

A hybrid of recurring relationship subscription, premium task fees, and optional user-funded model capacity.

### Recommended commercial model

> **Primary model**
>
> Base subscription + included monthly intelligence allowance + premium fees for high-cost or specialized work + optional connected provider accounts.

| **Revenue stream**            | **What the user receives**                                                                                                            | **Strategic role**                                               |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| **Free trial / introduction** | Limited relationship period, memory, and proactive check-ins; enough to experience continuity before payment.                         | Acquisition and trust formation.                                 |
| **Core subscription**         | Persistent identity, memory, text/voice-note conversation, basic proactivity, included model usage, and limited connected services.   | Predictable recurring revenue and everyday habit.                |
| **Partner subscription**      | Higher model allowance, advanced proactivity, more integrations, multi-model review, richer memory, and more active responsibilities. | Primary consumer paid tier.                                      |
| **Premium task fees**         | Clearly priced deep research, multi-step projects, external service work, or high-compute reasoning.                                  | Protects unit economics and aligns price with exceptional value. |
| **Connected-provider option** | Advanced users connect separately billed API accounts or local/private models; platform charges orchestration or platform fee.        | Reduces inference exposure and supports model choice.            |
| **Family/household plan**     | Individual private memories plus shared household responsibilities and common context.                                                | Higher ARPU and stronger network value.                          |
| **Future marketplace**        | Revenue share on premium skills, specialized agents, evaluation packs, and integrations.                                              | Ecosystem expansion after product-market fit.                    |

### Illustrative pricing hypotheses - not final

| **Tier**           | **Range**          | **Purpose**                                                                                                                |
|--------------------|--------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Core**           | \$12-\$20/month    | Everyday conversation, memory, modest proactive usage, one or two connected services.                                      |
| **Partner**        | \$30-\$50/month    | Higher reasoning allowance, multi-model consultations, voice calls when available, more responsibilities and integrations. |
| **Power / Family** | \$80-\$120/month   | Heavy usage, household support, premium models, larger task allowance, priority execution and privacy options.             |
| **Premium tasks**  | \$1-\$25+ per task | Price based on compute, external API cost, tool usage, duration, and risk; shown before execution when material.           |

These price bands are hypotheses for validation, not a recommendation to launch all tiers. The MVP should begin with one paid tier and transparent usage limits to avoid confusing users.

### Unit-economics controls

- **Model routing.** Use low-cost models for classification, memory extraction, and routine dialogue; reserve premium reasoning for high-value moments.

- **Context discipline.** Retrieve minimal relevant memory rather than sending full histories to every model.

- **Caching and reuse.** Cache stable summaries, embeddings, tool results, and evaluated outputs when privacy and freshness allow.

- **Cost-aware planning.** Estimate task cost before execution and ask approval when it crosses a user threshold.

- **Allowance design.** Translate token economics into understandable relationship or task allowances; do not expose raw token meters as the primary experience.

- **Provider redundancy.** Route around outages and price changes while maintaining quality floors.

- **User-funded capacity.** Permit advanced users to connect developer API accounts where supported, without making this mandatory for mainstream onboarding.

### Monetization integrity

Tips may be offered as an optional expression of appreciation, but they should not change emotional warmth, loyalty, response priority, or relationship status. A product that monetizes simulated affection undermines the trust proposition. The cleanest initial model is subscription plus disclosed task fees.

## 8. MVP definition

Validate durable relationship value, welcomed proactivity, and earned delegation with the smallest coherent product.

### Target user

Tech-forward, time-constrained professionals who already use one or more AI assistants, are comfortable connecting calendar and communication data, and want both a thinking partner and practical support. This segment is not the final market; it is the fastest learning cohort for model choice, cost, trust, and agent behavior.

### MVP product promise

> **Promise**
>
> One digital partner that remembers the user, checks in intelligently, helps think through life and work, and can gradually take over a small set of responsibilities after earning permission.

### In scope

| **Area**                   | **MVP scope**                                                                                                                                              |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Primary interface**      | Telegram private bot chat as the founder-alpha UI; the user must start the bot before it can continue or proactively follow up.                            |
| **Conversation**           | Text in both directions; inbound and outbound voice notes; images/files supported where useful; no native bot voice/video calls.                           |
| **Channel architecture**   | Telegram adapter plus canonical interaction envelope; no Telegram objects may enter identity, memory, reasoning, trust, learning, or skill-domain APIs.    |
| **Identity**               | One named agent with a stable baseline character, transparent bot/non-human disclosure, and persistent internal agent ID.                                  |
| **Memory**                 | External event history plus explicit typed memory with inspect, correct, delete, sensitivity, provenance, and do-not-remember controls.                    |
| **Reasoning**              | One production model provider initially, but through a provider interface; a second adapter is implemented before beta to prove portability.               |
| **Trust**                  | Deny-by-default action policy and responsibility-specific states from recommend to execute-with-approval; complete audit trail.                            |
| **Proactivity**            | One daily check-in and one event/follow-up trigger, with quiet hours, frequency controls, and useful/not-useful feedback.                                  |
| **Learning**               | Capture correction and outcome events; produce reviewable memory or procedure proposals rather than autonomous self-modification.                          |
| **Skill/action**           | One simulated skill from day one; one real low-risk skill added only after approval, audit, and rollback are working.                                      |
| **Control and operations** | Minimal owner console for webhook health, conversations, memory, trust, prompts/config, tests, traces, cost, feature flags, and deployment status.         |
| **Safety and privacy**     | Private 1:1 use, no groups in founder alpha, no high-risk actions, sensitive-data minimization in Telegram, encrypted owned storage, and incident logging. |

### Explicitly out of scope

- Open skill marketplace or third-party developer platform.

- Autonomous web research that installs new code or credentials without review.

- Broad browser control, purchases, money movement, medical decisions, or legal execution.

- Video avatar, photorealistic embodiment, romance-oriented features, or simulated exclusivity.

- Dedicated hardware, always-on microphones, or continuous camera sensing.

- Every major messaging platform. The founder alpha supports Telegram only; Slack, Teams, WhatsApp, WeChat, Instagram, and native applications remain adapter backlog.

- User reuse of consumer ChatGPT or Claude subscriptions as API capacity.

- Full family/household memory and shared-agent governance.

- Fine-tuning a proprietary foundation model.

### MVP success metrics

| **Metric**                 | **Initial validation target**                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Activation**             | ≥60% complete onboarding and return for a second meaningful conversation within 48 hours.                                                       |
| **Relationship formation** | ≥40% voluntarily teach or correct the agent at least three times in the first two weeks.                                                        |
| **Retention**              | Target ≥30% D30 retained in the qualified beta cohort; benchmark should be adjusted after private alpha.                                        |
| **Proactive value**        | ≥35% of agent-initiated messages receive a positive response or action; \<10% are muted, dismissed as irrelevant, or cause frequency reduction. |
| **Earned delegation**      | ≥25% of retained users advance at least one responsibility from recommend to prepare or execute-with-approval.                                  |
| **Task quality**           | ≥85% accepted or minimally edited outputs for the three MVP responsibilities.                                                                   |
| **Memory quality**         | \<5% material memory correction rate after the first month; all corrections are applied predictably.                                            |
| **Safety and trust**       | No silent permission expansion; 100% auditable action history; rapid rollback and incident review.                                              |
| **Economics**              | Model and infrastructure cost within a defined percentage of subscription revenue at target usage; exact threshold set during pricing tests.    |

### Pilot design

Run a staged cohort rather than an open launch: 20 internal/design partners, then 50-75 private-alpha users, then 200-500 invite-only beta users. Recruit users who already pay for AI and are willing to provide weekly qualitative feedback. The pilot should last long enough to test continuity; a two-week novelty test is insufficient.

## 9. Backlog post MVP

Expand only after the core relationship loop demonstrates retention, useful initiative, and progressive delegation.

| **Backlog theme**                      | **Candidate capabilities**                                                                                                                                                                                                     |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Horizon 1: deepen the relationship** | Improved proactive timing; richer emotional-context handling; shared rituals; conflict repair; adaptive interaction styles; real-time voice calls through a supported calling channel; portable relationship export/import.    |
| **Horizon 1: broaden useful work**     | Email and calendar execution; task/project management; travel planning; personal knowledge; calling businesses; document creation; controlled browser actions.                                                                 |
| **Horizon 1: provider choice**         | User-connected developer API accounts; additional hosted models; local/private models; model benchmarking and preference controls.                                                                                             |
| **Horizon 2: capability learning**     | Conversation-driven skill proposals, sandbox testing, evaluation criteria, versioning, rollback, and trust initialization.                                                                                                     |
| **Horizon 2: channels**                | Slack and Microsoft Teams adapters; WhatsApp, WeChat, Instagram and SMS/RCS subject to platform approval; real-time voice/calling adapter; owned mobile/desktop client; earbuds, car, smart speaker and wearable integrations. |
| **Horizon 2: household**               | Family plans, private versus shared memory, household responsibilities, child-safety design, consent, and multi-user conflict resolution.                                                                                      |
| **Horizon 2: ecosystem**               | Skill registry, developer SDK, revenue sharing, evaluation marketplace, verified tool providers, and capability certifications.                                                                                                |
| **Horizon 3: embodiment**              | Video calls, screen/camera understanding, optional avatar, spatial presence, and dedicated ambient hardware after evidence of need.                                                                                            |
| **Horizon 3: institutional extension** | Licensed relationship/trust framework for healthcare support, education, financial coaching, or enterprise assistants - only with domain-specific governance.                                                                  |

### Prioritization rules

- Does it increase durable user value rather than novelty or session length?

- Does it improve the relationship loop: understand, engage, act, evaluate, learn, or earn trust?

- Can it be added without compromising user control, privacy, or identity continuity?

- Does it materially improve retention, delegation, or unit economics?

- Is the feature better owned by the platform, supplied by a partner, or offered through the future ecosystem?

- Does it create a moat through accumulated outcomes and procedures, or merely copy a large platform feature?

### Open strategic questions

| **Question**                    | **Decision to resolve**                                                                                                                                                                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Consumer name and category**  | Should the market category be “digital partner,” “personal AI relationship,” “companion agent,” or a new term? Name and category testing should precede brand investment.                                                                                                         |
| **Relationship boundary**       | Is the product explicitly designed to strengthen human relationships, or can it position itself as a relationship in its own right? The safe and durable answer may be both, with strong anti-dependency design.                                                                  |
| **Messaging platform strategy** | Working decision: use Telegram private bot chat for the founder alpha because of its open Bot API, webhooks, rich media, proactive follow-up after onboarding, desktop/mobile reach, and rapid development path. Reassess platform risk and U.S. distribution before public beta. |
| **Agent personality**           | How much adaptation should occur automatically versus through user direction, and which core values should never adapt?                                                                                                                                                           |
| **Portability**                 | How much memory and identity portability can be offered while protecting safety policies, proprietary evaluation data, and experience quality?                                                                                                                                    |
| **Marketplace timing**          | When does extensibility accelerate value, and when does it create quality, privacy, and support complexity before product-market fit?                                                                                                                                             |

## 10. Project plan

A 24-week path to controlled beta, assuming a focused team and strict MVP boundaries.

### Planning assumptions

- Compact startup team of approximately 6-8 full-time contributors, with part-time legal, privacy, clinical/safety, and security advice.

- Use hosted model APIs and managed infrastructure; do not train a foundation model.

- Telegram private bot chat first. Build only a minimal owned control/operations console until the conversation and relationship loop are proven.

- Telegram is the committed founder-alpha channel. The adapter contract must be validated with a second mock or lightweight channel adapter before beta.

- Calendar read plus tightly controlled write actions; communication drafting but no autonomous sending in the initial beta.

- Invite-only launch to control cost, safety exposure, and feedback quality.

### Engineering delivery harness

The product manager should express product intent, acceptance criteria, constraints, risk, and evidence requirements rather than supervise code edits. The AI engineering system executes design, planning, implementation, testing, documentation, GitHub workflow, deployment, and maintenance through the repository-based harness defined in Section 11. The repository and automated evidence - not the chat session - remain the source of truth.

| **Stage**                        | **Required artifact or gate**                                                                                                                                                            |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Product requirement**       | Problem, user outcome, non-goals, acceptance criteria, data/privacy impact, trust impact, telemetry, rollout, and rollback are recorded in a versioned task file.                        |
| **2. Agent implementation plan** | Coding agent identifies impacted contracts, architecture rules, migrations, tests, dependencies, and deployment risks before modifying code.                                             |
| **3. Isolated implementation**   | Change is created on a branch with small commits; architecture tests prevent Telegram, provider, or database details from leaking across boundaries.                                     |
| **4. Automated verification**    | Formatting, type checks, unit tests, adapter contract tests, integration tests, security scans, prompt/model evaluations, and synthetic conversation regressions run in CI.              |
| **5. Staging conversation test** | The staging Telegram bot executes scripted and exploratory conversations; traces, messages, memory changes, trust decisions, costs, and failures are captured.                           |
| **6. Review package**            | The harness produces a human-readable report: requirement coverage, changed behavior, test results, evaluation deltas, screenshots/transcripts, risks, and recommended rollout decision. |
| **7. Product approval**          | The product owner reviews outcomes and explicitly approves, requests revision, or rejects. High-impact changes require a second reviewer.                                                |
| **8. Controlled deployment**     | Deploy behind feature flags or a canary cohort; run smoke tests; monitor errors, latency, cost, and behavioral metrics; automatically roll back on defined thresholds.                   |
| **9. Post-deployment learning**  | Production evidence is linked back to the requirement. Failures become regression tests; successful behavior may inform memory, procedure, or trust-policy improvements.                 |

### 24-week execution plan

| Weeks | Phase | Primary deliverables |
|---|---|---|
| W1-2 | **Phase 0 - Walking skeleton and engineering harness** | Architecture decision records; repository rules; canonical interaction contract; all service interfaces and stubs; Telegram bot registration; secure webhook; outbound sender; CI/CD; staging and production bots; contract, unit, and security tests; tracing and rollback. |
| W3-6 | **Phase 1 - Communication, evidence, and identity** | Reliable text and voice-note loop; media normalization; queues and rate-limit handling; event store; replay; cost telemetry; persistent internal user/agent IDs; baseline personality; onboarding; minimal owner console. |
| W7-12 | **Phase 2 - Memory and portable reasoning** | Typed memory with correction, deletion, and provenance; retrieval; conversation summaries; first provider adapter; second provider contract implementation; model-routing basics; regression conversation suite; privacy and prompt-injection controls. |
| W13-16 | **Phase 3 - Trust, proactivity, and one bounded skill** | Trust ledger; approval and audit workflow; proactive scheduler and event trigger; quiet hours and interruption budget; outcome and evaluation events; one simulated skill and one low-risk real skill behind explicit approval and rollback. |
| W17-20 | **Phase 4 - Founder use and private alpha** | Daily personal use; synthetic and real conversation evaluation; incident replay; prompt/model changes through the harness; 20-75 design partners only after founder reliability; tuning for memory, personality, timing, cost, and trust behavior. |
| W21-24 | **Phase 5 - Invite-only beta decision** | Expand to 200-500 users only if evidence supports it; paid-plan experiment; onboarding; second-channel feasibility; vendor redundancy; security/privacy review; product-market-fit evidence; post-MVP roadmap. |

### Core team

| **Role**                                    | **Accountability**                                                                                                    |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| **Founder / Product lead**                  | Vision, user research, scope, partnerships, pricing, fundraising, and final product decisions.                        |
| **Technical lead / architect**              | System architecture, security boundaries, provider abstraction, reliability, and engineering quality.                 |
| **2 agent/backend engineers**               | Orchestration, memory, trust, proactivity, tools, integrations, event systems, and API platform.                      |
| **1 product/full-stack or mobile engineer** | Owned application, messaging channel integration, notifications, voice surfaces, and control center.                  |
| **1 product designer / researcher**         | Conversation design, relational UX, onboarding, trust transparency, user studies, and brand exploration.              |
| **1 applied AI / evaluation engineer**      | Model routing, prompt/context systems, offline evaluation, outcome measurement, red teaming, and cost optimization.   |
| **Fractional specialists**                  | Privacy counsel, security review, AI safety/mental-health expertise, finance/operations, and customer support design. |

### Decision gates

| **Gate**             | **Exit criterion**                                                                                                                                                        |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Gate 1 - Week 2**  | Proceed only when the Telegram staging and production bots complete a secure, traced, idempotent text loop and the channel adapter contract contains no agent-core logic. |
| **Gate 2 - Week 6**  | Every interaction is replayable; identity and memory survive model-provider switching; all major component stubs are covered by contract and architecture tests.          |
| **Gate 3 - Week 12** | Founder use demonstrates inspectable memory, deny-by-default trust, controlled proactivity, and a complete approve/execute/audit/rollback cycle for one bounded skill.    |
| **Gate 4 - Week 20** | Private alpha must show evidence that proactive interactions are welcomed and users are voluntarily increasing delegation.                                                |
| **Gate 5 - Week 24** | Expand only if retention, task quality, safety, and unit-economics trends support a paid beta; otherwise narrow or reposition before scaling.                             |

### Top execution risks and mitigations

| **Risk**                        | **Mitigation**                                                                                                                                                                                                     |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Scope explosion**             | Hold a written non-goals list; every feature must prove one of the three MVP hypotheses.                                                                                                                           |
| **Poor proactive timing**       | Start with low frequency, explicit user controls, interruption budgets, and rapid feedback loops.                                                                                                                  |
| **Memory errors or creepiness** | Use provenance, confidence thresholds, sensitive-memory rules, visible correction, and “why this was used” explanations.                                                                                           |
| **Inference cost**              | Instrument from day one; use routing, summaries, context limits, caching, and usage allowances.                                                                                                                    |
| **Platform dependency**         | Treat Telegram strictly as the first adapter; own all identity, memory, trust, prompts, events, billing, and evaluation data; maintain export and a tested mock/secondary adapter; monitor API and policy changes. |
| **Model inconsistency**         | Use stable agent policy, evaluated prompts, model-specific adapters, fallbacks, and regression testing.                                                                                                            |
| **Emotional safety**            | Avoid engagement optimization as the sole KPI; establish expert review, escalation paths, and anti-manipulation requirements.                                                                                      |
| **Premature ecosystem work**    | Do not build a marketplace before a compelling first-party relationship experience and repeatable capability model exist.                                                                                          |

### Immediate next actions

1. Conduct 12-15 interviews with heavy AI users to test the relationship proposition, not merely feature interest.

2. Create the Telegram bot and prove the production walking skeleton: start link, secure webhook, canonical envelope, dummy component calls, outbound queue, traced response, and replay.

3. Write and enforce the channel-adapter contract. Document Telegram onboarding, proactive-message, media, group, calling, privacy, rate-limit, billing, and policy constraints; build a mock second adapter to prove separation.

4. Scaffold identity, memory, reasoning, trust, proactivity, learning/evaluation, skills/actions, and governance interfaces. Define the enrichment sequence and exit tests before adding deep logic.

5. Establish the agent-portable engineering harness and initial role separation: ChatGPT or Gemini for planning; Cursor for repository editing, implementation, and local validation; Manus for independent review and portability validation; and GitHub for backlog, workflow, evidence, approvals, and change history. Add the task specification template, architecture tests, adapter contracts, synthetic conversation suite, model evaluations, staging bot, CI/CD, review report, feature flags, and rollback.

6. Build a cost model for Telegram traffic, speech processing, memory retrieval, model calls, proactive messages, and task execution; continue consumer naming research while retaining “Zero-Trust Agent Framework” as the internal architecture name.

## 11. Development and maintenance process

An agent-first delivery model in which the product owner defines the requirement and evidence of success, while AI executes the software lifecycle end to end.

### Operating model

Project Continuum will adopt the operating principles documented in OpenAI's Harness Engineering experience report [14]. The governing idea is simple: “Humans steer. Agents execute.” The human works at the product and policy layer; engineering agents work at the planning, design, code, test, review, release, and maintenance layers. Planning, implementation, independent review, and work management are separate roles with explicit handoffs. All production code, tests, CI configuration, documentation, observability assets, deployment tooling, and repository utilities should be generated and maintained by agents rather than manually edited by the product owner.

*Important interpretation: the OpenAI article is an engineering experience report, not a formal certification standard. “Strictly follow” therefore means that Project Continuum adopts its documented principles - repository knowledge as the system of record, agent legibility, mechanically enforced architecture, agent-to-agent review, evidence-driven validation, progressive autonomy, and continuous cleanup - while adding explicit zero-trust controls for production access and irreversible actions.*

### Division of responsibility

| **Role**                               | **Primary responsibility**                                                                                                                                                                                                                  |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Product owner**                      | Define the user problem, desired outcome, priority, acceptance criteria, constraints, non-goals, risk classification, budget, and deployment policy. Review only exceptions, material tradeoffs, or final evidence when policy requires it. |
| **AI product and architecture agents** | Convert intent into a product specification, clarify ambiguity, evaluate solution options, create the design, identify risks, and produce an execution plan.                                                                                |
| **AI implementation agents**           | Create or modify application code, tests, migrations, CI, infrastructure, telemetry, documentation, feature flags, and internal tools in an isolated worktree.                                                                              |
| **AI review and validation agents**    | Review the change independently, run architecture, security, privacy, reliability, performance, model-quality, and end-to-end tests, and reject work that lacks evidence.                                                                   |
| **AI release and operations agents**   | Open and maintain the GitHub pull request, remediate CI failures, merge under policy, deploy to staging and production, validate the release, monitor health, and roll back when necessary.                                                 |
| **Human specialist, exception only**   | Provide judgment for unresolved product choices, security or legal exceptions, high-impact data changes, financial exposure, or any issue that policy explicitly reserves for a person.                                                     |

### Initial tool-role operating model

The workflow is role-based rather than vendor-locked. The following assignments are the initial founder defaults; a tool may be replaced when the substitute satisfies the same repository access, evidence, security, and approval contracts.

| **Initial role and tool**                             | **Responsibility and operating boundary**                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Planning agent - ChatGPT or Gemini**                | Convert the proposal, approved requirements, and versioned repository artifacts into product specifications, solution designs, and execution plans. In the initial workflow, the planner is not granted direct local-repository access; it must identify assumptions and may not claim unobserved local state. Its output becomes authoritative only after product-owner approval and storage in GitHub. |
| **Implementation and editor agent - Cursor**          | Operate in the local repository and isolated branch or worktree; validate current state; implement, test, document, and prepare the pull request and evidence. Cursor must record material deviations from the approved plan rather than silently changing product intent.                                                                                                                               |
| **Independent review agent - Manus**                  | Review repository artifacts, pull-request changes, CI results, risks, and maintainability independently. Run the portability validation using repository instructions rather than the planner conversation. Manus may recommend approval or rejection but may not merge or deploy without authority.                                                                                                     |
| **Management platform and system of record - GitHub** | Manage backlog and priorities through Issues and Projects; preserve branches, commits, pull requests, CI checks, approvals, release records, and the audit trail. GitHub records are authoritative over vendor-specific chats or project memories.                                                                                                                                                       |

**Cross-tool handoff rule.** An approved plan must be committed or linked in GitHub before implementation. Cursor performs current-state validation and records deviations; Manus reviews from repository and pull-request evidence rather than relying on the original planning chat. Routine low-risk work may combine roles only when policy permits, while architecture, security, privacy, and other material changes retain independent review.

### What the product owner provides

The target interaction is requirement-only. The product owner should not need to select files, prescribe implementation details, review individual code edits, or manually move work between development stages. A lightweight requirement can begin in natural language; the agent converts it into the structured contract below and asks only for decisions that materially affect the product.

| **Requirement field**            | **Minimum input or default behavior**                                                                                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Problem and user outcome**     | What is wrong today, who experiences it, and what should be measurably better after delivery.                                                       |
| **Acceptance criteria**          | Observable behaviors and evidence required for completion. The AI proposes criteria when they are omitted.                                          |
| **Constraints and non-goals**    | Privacy, security, latency, cost, platform, schedule, compatibility, and scope boundaries.                                                          |
| **Risk and data classification** | Low, medium, or high risk; data sensitivity; reversibility; and whether the change can affect money, identity, permissions, or user communications. |
| **Priority and timing**          | Relative priority and any real deadline. The AI creates the detailed project and execution plan.                                                    |
| **Deployment authority**         | Standing policy for automatic merge/deployment or the approval gate required for this class of change.                                              |

### End-to-end AI delivery lifecycle

Every requirement follows one traceable workflow. The agent may iterate within a stage without human involvement, but it cannot silently skip required artifacts or evidence.

| **Stage**                         | **AI-owned activity and required output**                                                                                                                                                                         |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Intake and normalization**   | Read the requirement, inspect related product specifications and history, identify ambiguity, and produce a versioned requirement record with proposed acceptance criteria.                                       |
| **2. Current-state validation**   | Build the current codebase, run baseline tests, reproduce the issue or establish the baseline behavior, and capture logs, screenshots, video, traces, or benchmark results as applicable.                         |
| **3. Solution and design**        | Generate viable options, analyze tradeoffs, choose a recommended approach, update architecture and data-flow documentation, and record consequential decisions.                                                   |
| **4. Project and execution plan** | Break the change into ordered tasks, dependencies, migration and rollback steps, test strategy, risk controls, and completion checkpoints. Store the active plan in the repository.                               |
| **5. Isolated implementation**    | Create a branch and isolated worktree, implement the change, and generate all related tests, migrations, infrastructure, feature flags, telemetry, runbooks, and documentation.                                   |
| **6. Local self-validation**      | Build and run formatting, static analysis, unit, integration, contract, security, privacy, cost, and reliability checks. Launch the app and exercise the affected journeys directly.                              |
| **7. Independent agent review**   | Request architecture, security, test, product-quality, and maintainability reviews from separate agents. Respond to findings and repeat until reviewers are satisfied.                                            |
| **8. End-to-end evidence**        | Run synthetic Telegram conversations and relevant browser or API journeys; inspect logs, metrics, and traces; compare before-and-after behavior; and record validation media when useful.                         |
| **9. Validation dossier**         | Create a concise evidence package containing requirement traceability, design, plan, code summary, tests run, results, known limitations, risk assessment, rollback plan, and deployment recommendation.          |
| **10. GitHub delivery**           | Commit and push the code, open the pull request, attach the dossier, respond to agent or human feedback, remediate CI failures, and keep the pull request synchronized until merge-ready.                         |
| **11. Merge and deployment**      | Merge according to policy, deploy automatically to staging, run smoke and regression tests, promote to production when authorized, verify the live service, and roll back automatically if release criteria fail. |
| **12. Closeout and learning**     | Update the product specification, architecture, completed execution plan, release notes, quality score, technical-debt register, and reusable harness rules so the lesson compounds into future work.             |

### Repository as the system of record

The AI must not depend on context that exists only in a chat window, a person's memory, or an external document. A short AGENTS.md acts as a map rather than a giant manual, and points agents to versioned sources of truth inside the repository. This follows OpenAI's progressive-disclosure pattern [14].

- AGENTS.md - concise navigation map, working rules, commands, and links to deeper documents.

- ARCHITECTURE.md and docs/design-docs/ - system boundaries, domain layering, data flows, interfaces, and architecture decision records.

- docs/product-specs/ - current product requirements, user journeys, acceptance criteria, and non-goals.

- docs/exec-plans/active and completed/ - executable plans, progress, decisions, evidence, and completion records.

- docs/quality/, RELIABILITY.md, SECURITY.md, PRIVACY.md, and COST.md - mechanical standards, quality scores, service objectives, threat controls, and unit-economics constraints.

- docs/runbooks/ and docs/generated/ - deployment, rollback, incident response, schemas, APIs, configuration, and generated operational references.

- evals/, tests/, and fixtures/ - model evaluations, synthetic conversations, regression suites, contract tests, and reproducible failure cases.

- .github/workflows/, scripts/, and infrastructure/ - CI, release, deployment, observability, repository maintenance, and recovery automation.

### Harness capabilities required

| **Capability**                          | **Purpose**                                                                                                                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Deterministic repository bootstrap**  | One command creates dependencies, configuration, local services, seed data, and a runnable environment without undocumented manual setup.                                      |
| **Isolated worktree environments**      | Each change has its own app instance, test data, logs, metrics, and traces so agents can work concurrently without contaminating one another.                                  |
| **Application legibility**              | Agents can drive Telegram test conversations, APIs, and any owned web console; inspect screenshots and state; and query runtime events directly.                               |
| **Observability legibility**            | Structured logs, metrics, traces, cost events, model calls, tool calls, and trust decisions are queryable by the agent during development and after deployment.                |
| **Mechanical architecture enforcement** | Custom linters and structural tests enforce allowed dependencies, boundary parsing, schemas, naming, logging, file-size, security, and reliability invariants.                 |
| **Evaluation and test harness**         | Unit, integration, contract, end-to-end, synthetic conversation, memory, trust, proactive-engagement, model-quality, safety, latency, and cost tests run reproducibly.         |
| **GitHub and review automation**        | Agents can create branches, commits, pull requests, review comments, status checks, merges, release notes, and issue links without copy-and-paste handoffs.                    |
| **Deployment and recovery interface**   | Agents can deploy to isolated environments, staging, and production under policy; run health checks; inspect telemetry; pause rollout; and execute tested rollback procedures. |
| **Secrets and permissions broker**      | Short-lived credentials and least-privilege roles are issued to the appropriate agent and environment. Secrets never live in prompts, source files, or validation documents.   |
| **Artifact and evidence generator**     | Every change automatically produces design, plan, test results, validation evidence, risk record, deployment record, and post-release verification documentation.              |

### Autonomy and deployment policy

The desired steady state is that the product owner states the requirement and the AI completes the delivery. That outcome should be earned through the same zero-trust principle used by the product itself. The harness begins with narrow permissions and expands autonomy when evidence demonstrates that the workflow is reliable.

| **Change class**                      | **Default authority**                                                                                                                                                                                                               |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Development and test environments** | AI may create, modify, test, reset, and redeploy automatically inside isolated environments.                                                                                                                                        |
| **Staging**                           | AI may deploy automatically after required checks pass and may repeat deployment while resolving failures.                                                                                                                          |
| **Low-risk production changes**       | AI may merge and deploy automatically once the repository has demonstrated stable tests, rollback, observability, and successful prior releases for this class of change.                                                           |
| **Medium-risk production changes**    | AI prepares the full validation dossier and requests one product-owner approval for promotion. No code-level review is required unless requested.                                                                                   |
| **High-risk or irreversible changes** | Explicit human approval remains mandatory for security boundaries, identity and permission models, destructive data migration, billing or money movement, legal commitments, sensitive-data expansion, and untested rollback paths. |
| **Emergency remediation**             | AI may diagnose, prepare, test, and stage a fix immediately. Production action follows the pre-approved incident policy; the system records every action and automatically produces the incident report.                            |

### Definition of done

- The delivered behavior satisfies each acceptance criterion and the evidence is linked to the requirement.

- Architecture, security, privacy, reliability, cost, model-quality, and maintainability checks pass at the level required by the change risk.

- Automated tests cover the change and reproduce any corrected defect; UI or conversational behavior is validated end to end when applicable.

- The repository documentation, diagrams, schemas, runbooks, and execution plan reflect the actual implementation.

- The GitHub pull request contains the validation dossier, review history, test outputs, known limitations, rollout plan, and rollback plan.

- The change is deployed to its authorized environment, live health is verified, observability is clean, and rollback remains available.

- Any new lesson is converted into a reusable test, lint, tool, document, fixture, or policy rather than remaining only in conversation history.

### Maintenance and continuous improvement

Maintenance is not a separate manual phase. Agents continuously inspect the product and the repository, open focused pull requests, validate repairs, and deploy approved changes. Human feedback is translated into acceptance criteria or harness improvements so the same issue becomes less likely to recur.

| **Cadence or trigger**  | **Agent-owned maintenance activity**                                                                                                                                                                                 |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Continuous**          | Watch service health, failed Telegram deliveries, model and tool errors, latency, costs, security signals, deployment health, and trust-policy violations. Diagnose and recover within the approved incident policy. |
| **After every release** | Run production smoke tests, compare telemetry with baseline, verify migrations and feature flags, update release evidence, and automatically roll back when release criteria are breached.                           |
| **Daily**               | Scan failed tests, flaky behavior, stale branches, documentation drift, architecture violations, unresolved alerts, dependency advisories, and recurring user complaints; open targeted remediation pull requests.   |
| **Weekly**              | Run full synthetic conversation and model evaluations, review quality scores, inspect cost and performance trends, refresh technical debt priorities, and execute small garbage-collection refactors.                |
| **Monthly**             | Reassess architecture boundaries, permissions, deployment policies, model/provider choices, data retention, reliability objectives, and whether additional autonomy has been earned.                                 |
| **New failure pattern** | Create a reproducible fixture, add a regression test or evaluation, repair the implementation, and update the relevant rule, documentation, or tool so future agents can detect the problem mechanically.            |

### Escalation policy

The AI should proceed autonomously unless one of the following conditions applies:

- Two materially different product interpretations remain valid and choosing one changes the intended user outcome.

- A required action exceeds the standing permission, risk, cost, data, or deployment policy.

- Validation reveals a tradeoff that cannot satisfy the documented acceptance criteria simultaneously.

- The change is irreversible, has no tested rollback, or could materially affect user identity, permissions, money, legal position, safety, or sensitive data.

- Required credentials, external approvals, or contractual rights do not exist.

- The harness itself cannot observe or test the affected behavior reliably; the missing capability must be added before the work can be considered complete.

### Implementation sequence for the engineering harness

| **Harness stage**                             | **Exit condition**                                                                                                                                                                                             |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **H0 - Repository bootstrap**                 | Agent-generated repository structure, short AGENTS.md map, architecture rules, CI, formatting, test commands, environment setup, documentation tree, and GitHub integration are operational.                   |
| **H1 - Requirement to pull request**          | A natural-language requirement reliably produces a specification, design, execution plan, code, tests, documentation, validation dossier, and a passing GitHub pull request without manual code edits.         |
| **H2 - Application and telemetry legibility** | The agent can launch an isolated instance, run synthetic Telegram conversations, inspect application state, and query logs, metrics, traces, model calls, cost, and trust decisions.                           |
| **H3 - Staging deployment loop**              | The agent can merge under policy, deploy to staging, run end-to-end validation, remediate failure, redeploy, and produce release evidence automatically.                                                       |
| **H4 - Controlled production delivery**       | Low-risk changes can be promoted with one product approval; rollback and post-deployment verification are automated and proven through drills.                                                                 |
| **H5 - Progressive production autonomy**      | Selected low-risk change classes earn automatic merge and deployment based on measured success, while medium and high-risk categories retain explicit gates.                                                   |
| **H6 - Self-maintaining repository**          | Doc gardening, quality scoring, dependency maintenance, evaluation refresh, technical-debt cleanup, incident learning, and drift correction run on recurring schedules and open evidence-backed pull requests. |

### H0 repository bootstrap clarification

H0 is the controlled initialization of the repository and engineering harness. It creates the minimum durable operating system that allows coding agents to work consistently, safely, and audibly before meaningful Continuum product implementation begins. H0 also proves the initial planner-to-editor-to-reviewer handoff using repository artifacts. H0 is not the Telegram walking skeleton and does not deliver user-facing product behavior.

| **H0 area**               | **Repository-bootstrap requirement**                                                                                                                                                                                                                                                                                                                     |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Objective                 | Create a deterministic, auditable, and agent-portable repository that supports a planner-to-editor-to-reviewer handoff and can be used by ChatGPT, Gemini, Cursor, Manus, Codex, or another qualified agent without making any one tool a runtime dependency.                                                                                            |
| In scope                  | Repository structure; short AGENTS.md navigation map; architecture and dependency rules; documentation hierarchy; tool-role and handoff rules; issue and pull-request templates; bootstrap, formatting, static-check, and test commands; minimal CI; secret checks; and GitHub workflow integration.                                                     |
| Required artifacts        | AGENTS.md, ARCHITECTURE.md, SECURITY.md, PRIVACY.md, COST.md, product and design templates, architecture-decision records, active and completed execution-plan folders, validation templates, scripts, tests, fixtures, and GitHub workflow definitions.                                                                                                 |
| Execution record          | A GitHub requirement issue, approved bootstrap plan, implementation branch, small commits, pull request, CI outputs, validation dossier, merge record, and completed execution plan linked to one another.                                                                                                                                               |
| Exit evidence             | From a clean clone, one documented bootstrap command succeeds, one documented test command passes, CI is green, no secrets or cloud resources are introduced, and a second agent can follow AGENTS.md and validate the repository without undocumented context. The planner, editor, reviewer, and GitHub records are linked through the H0 audit chain. |
| Approval and authority    | The product owner approves the H0 plan and the pull-request merge. Planning agents may propose artifacts; Cursor may implement and validate on an isolated branch after approval; Manus may review and perform portability validation; no agent may push directly to main, merge, deploy, or create infrastructure without explicit authorization.       |
| Initial tool-role handoff | ChatGPT or Gemini creates or revises the plan; Cursor validates repository state and implements from approved repository artifacts; Manus independently reviews and runs portability validation; GitHub records backlog, artifacts, CI, approvals, and history. Named tools are replaceable when equivalent controls are met.                            |
| Explicit non-goals        | No Telegram bot, model-provider integration, production database, cloud infrastructure, deployment environment, autonomous production release, or substantive Continuum product behavior is implemented during H0.                                                                                                                                       |

### Audit and change-control model

The strategic proposal defines intent, principles, scope, and stage-level exit conditions. Detailed execution truth is maintained in GitHub. Prompts, chats, local editor sessions, and vendor project memories may initiate or support work, but they are not authoritative records and must not be the only place where a decision, plan, review finding, or result exists.

- Proposal baseline - version the strategic proposal when product intent, governance, stage definitions, or major constraints change.

- Requirement issue - record the requested outcome, acceptance criteria, non-goals, risk, data impact, evidence requirements, and deployment authority.

- Design and decisions - store the recommended solution, alternatives, tradeoffs, data flows, and consequential architecture decisions in versioned repository documents.

- Active execution plan - maintain ordered work, dependencies, tests, checkpoints, decisions, deviations, and rollback steps under docs/exec-plans/active/.

- Implementation history - use an isolated branch, small commits, a linked pull request, automated checks, review findings, and remediation history.

- Validation dossier - capture requirement coverage, commands and tests run, results, screenshots or transcripts when relevant, risks, limitations, rollout, rollback, and the recommended release decision.

- Tool-role and handoff record - identify the planning agent, implementation agent, independent reviewer, and any material tool or model change in the issue, pull request, or validation dossier; link durable artifacts rather than relying on vendor chat history.

- Closeout record - move the final plan to docs/exec-plans/completed/, link the merge commit and release evidence, update specifications and architecture, and convert lessons into reusable tests, rules, fixtures, tools, or policies.

**Minimum traceability chain:** proposal version -\> GitHub requirement -\> tool-role assignment -\> design and ADRs -\> active execution plan -\> branch and pull request -\> independent review -\> CI and validation evidence -\> merge or release -\> completed plan and lessons learned.

Artifacts are amended through normal Git history rather than overwritten without explanation. Every material artifact should identify its related issue, pull request, final commit, status, owner, and date.

### Tooling position and substitution policy

The harness is role-based and agent-portable. The initial founder workflow uses ChatGPT or Gemini as the planning agent, Cursor as the primary repository editor and implementation agent, Manus as the independent reviewer and portability validator, and GitHub as the management platform and authoritative record. Codex remains a compatible alternative execution or review agent rather than a mandatory dependency. Any tool may be substituted only when it can satisfy the same repository access, shell and test, evidence, security, and approval contracts. Tool-specific memory or chat context never overrides repository policy, required evidence, or approval gates.

### Expected product-owner experience

**The intended interaction is: “Here is the requirement and how I will judge success.” ChatGPT or Gemini helps produce the requirement, solution design, and execution plan. After product-owner approval and GitHub recording, Cursor validates the current repository state, implements and tests the change in isolation, and prepares the pull request and validation evidence. Manus independently reviews the repository evidence and performs portability or quality validation. GitHub maintains the backlog, artifacts, CI checks, approvals, merge history, and release record. The product owner is interrupted only for material product judgment or an approval that policy has deliberately reserved for a human.**

### Document governance and version history

**Current version: 0.3.** The strategic proposal is revised only when product intent, governance, stage definitions, major constraints, or the default tool-role operating model changes. Detailed engineering execution history remains in the GitHub repository.

| **Version and date** | **Material change**                                                                                                                                                                                                                                                                                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.1 - July 19, 2026  | Initial product strategy, MVP definition, architecture, project plan, and agent-first engineering-harness operating model.                                                                                                                                                                                                                    |
| 0.2 - July 21, 2026  | Clarified H0 repository-bootstrap scope, approval boundaries, repository audit trail, document versioning, and the separation between strategic intent and GitHub execution records.                                                                                                                                                          |
| 0.3 - July 21, 2026  | Established the initial role-based tool operating model: ChatGPT or Gemini for planning, Cursor for repository editing and implementation, Manus for independent review and portability validation, and GitHub for management and the authoritative audit trail. Clarified cross-tool handoffs, substitution policy, and tool-role recording. |

## Appendix: Market references and proposal notes

*Accessed July 19, 2026. Product capabilities and policies change frequently; refresh this section before external circulation.*

**[1] OpenAI - Memory FAQ -** <https://help.openai.com/en/articles/8590148>

**[2] OpenAI - Scheduled Tasks in ChatGPT -** <https://help.openai.com/en/articles/10291617-tasks-in-chatgpt>

**[3] Anthropic - Understanding Claude’s personalization features -** <https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features>

**[4] The Verge - Google Gemini scheduled actions, linking Google’s announcement -** <https://www.theverge.com/news/681762/google-gemini-scheduled-actions-planned-tasks>

**[5] Replika - Product website and features -** <https://replika.com/>

**[6] Character.AI - Introducing Character Calls -** <https://blog.character.ai/introducing-character-calls/>

**[7] OpenAI - What is ChatGPT Plus? (API billed separately) -** <https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus>

**[8] Anthropic - How can I access the Claude API? -** <https://support.claude.com/en/articles/8114521-how-can-i-access-the-claude-api>

[9] Telegram - Bots: An introduction for developers - https://core.telegram.org/bots

[10] Telegram - Bot API reference - https://core.telegram.org/bots/api

[11] Telegram - Bot features and monetization - https://core.telegram.org/bots/features

[12] Telegram - Bot FAQ, rate limits and group privacy behavior - https://core.telegram.org/bots/faq

[13] Telegram - General FAQ, cloud chats and Secret Chats - https://telegram.org/faq

[14] OpenAI - Harness engineering: leveraging Codex in an agent-first world - https://openai.com/index/harness-engineering/

### Proposal status

This document is a strategic working proposal and implementation blueprint, not a final product requirements document or investment memorandum. Telegram capabilities and policies, pricing, legal positioning, safety controls, technical estimates, and market claims require continuing validation before public release. The Telegram-first decision applies to the founder alpha; the product architecture remains channel-independent. Detailed execution plans, evidence, completion records, and change history are maintained in GitHub rather than duplicated here.
