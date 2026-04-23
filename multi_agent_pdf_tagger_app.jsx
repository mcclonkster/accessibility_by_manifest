import React, { useMemo, useState } from "react";
import { motion } from "framer-motion";
import {
  AlertTriangle,
  Bot,
  BrainCircuit,
  CheckCircle2,
  Code2,
  Download,
  Eye,
  FileText,
  GitBranch,
  KeyRound,
  Loader2,
  PlugZap,
  RefreshCw,
  ShieldCheck,
  Upload,
  Workflow,
} from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const agents = [
  {
    name: "Document Intake Agent",
    modelRole: "local-vision-or-text-model",
    endpoint: "/api/agents/document-intake",
    role: "Detects page count, existing tags, scans, embedded text, fonts, links, annotations, and obvious file-level blockers.",
    input: "Raw PDF + extraction report",
    output: "intake_report.json",
  },
  {
    name: "Reading Order Agent",
    modelRole: "local-layout-model + LLM",
    endpoint: "/api/agents/reading-order",
    role: "Builds a proposed logical reading order from headings, columns, lists, figures, tables, headers, and footers.",
    input: "Page layout blocks + OCR/text spans",
    output: "reading_order.json",
  },
  {
    name: "Structure Tag Agent",
    modelRole: "local-llm",
    endpoint: "/api/agents/structure-tags",
    role: "Assigns semantic tags such as Document, H1, H2, P, L, LI, Figure, Table, TH, TD, Link, and Artifact.",
    input: "Reading order + extracted text + layout hints",
    output: "tag_plan.json",
  },
  {
    name: "Alt Text Agent",
    modelRole: "local-vision-model + LLM",
    endpoint: "/api/agents/alt-text",
    role: "Finds meaningful visuals, drafts alt text, and marks decorative or repeated visuals as artifacts.",
    input: "Figure crops + surrounding text",
    output: "alt_text_plan.json",
  },
  {
    name: "Table Agent",
    modelRole: "local-llm",
    endpoint: "/api/agents/tables",
    role: "Checks table headers, row and column relationships, merged cells, and cell reading path.",
    input: "Detected tables + cell text + geometry",
    output: "table_plan.json",
  },
  {
    name: "Validation Agent",
    modelRole: "rules + local-llm reviewer",
    endpoint: "/api/agents/validation",
    role: "Runs machine checks, compares the structure tree with visible content, and sends uncertain items to human review.",
    input: "Tagged PDF draft + all agent reports",
    output: "validation_report.json",
  },
];

const collaborationPhases = [
  {
    name: "Deterministic evidence pass",
    purpose: "Code extracts facts the agents must respect: text spans, coordinates, font sizes, page order, image boxes, table candidates, links, annotations, and existing tags.",
  },
  {
    name: "Specialist proposal pass",
    purpose: "Each AI agent proposes only its part of the tag plan and cites the deterministic evidence it used.",
  },
  {
    name: "Cross-check pass",
    purpose: "Agents review each other for contradictions: reading order vs. headings, figures vs. alt text, tables vs. structure tags, artifacts vs. meaningful content.",
  },
  {
    name: "Deterministic rule pass",
    purpose: "Code checks the revised plan for missing roots, skipped content, duplicate claims, orphan nodes, invalid nesting, table header gaps, and unreviewed low-confidence items.",
  },
  {
    name: "Repair pass",
    purpose: "The responsible agent receives the specific failed checks and patches the tag plan without rewriting unrelated parts.",
  },
  {
    name: "Convergence gate",
    purpose: "The workflow stops when deterministic blockers are resolved or the remaining items are explicitly sent to human review.",
  },
];

const deterministicChecks = [
  "Every visible text span is tagged or intentionally artifacted.",
  "The document has one valid root structure.",
  "Headings follow a plausible hierarchy without unexplained jumps.",
  "List containers include list items and labels/bodies when present.",
  "Figures have approved alt text or are marked decorative with a reason.",
  "Tables have header relationships or are flagged for manual repair.",
  "Links preserve visible text, target, and annotation relationship.",
  "Artifacts do not hide unique meaningful content.",
  "Reading order does not cross columns incorrectly.",
  "Low-confidence or conflicting decisions are routed to review.",
];

const crossCheckMatrix = [
  {
    reviewer: "Reading Order Agent",
    checks: "Structure Tag Agent",
    question: "Does the tag tree follow the visual/logical reading order?",
  },
  {
    reviewer: "Structure Tag Agent",
    checks: "Alt Text Agent",
    question: "Are figures tagged semantically and are decorative choices justified?",
  },
  {
    reviewer: "Table Agent",
    checks: "Structure Tag Agent",
    question: "Are tables represented as tables rather than layout text?",
  },
  {
    reviewer: "Validation Agent",
    checks: "All agents",
    question: "Which claims fail deterministic checks or need human review?",
  },
];

const pipeline = [
  "Upload PDF",
  "Deterministic analysis",
  "AI cross-check rounds",
  "Repair tag plan",
  "Human review",
  "Write PDF tags",
  "Validate output",
  "Export package",
];

const workflowIndex = {
  idle: 0,
  uploaded: 1,
  analyzing: 1,
  agentsRunning: 2,
  repairing: 3,
  reviewNeeded: 4,
  tagging: 5,
  validating: 6,
  readyToExport: 7,
  failed: 0,
};

const backendHooks = [
  {
    name: "Check PDF tagging adapter",
    method: "GET",
    endpoint: "/api/pdf/tag/health",
    purpose: "Confirm that the backend component responsible for writing approved tags into a PDF is available.",
  },
  {
    name: "Analyze PDF",
    method: "POST",
    endpoint: "/api/pdf/analyze",
    purpose: "Extract text, page geometry, images, links, annotations, tables, existing tags, and scan/OCR status.",
  },
  {
    name: "Run AI agents",
    method: "POST",
    endpoint: "/api/agents/run",
    purpose: "Send deterministic evidence through the agent team, run cross-check rounds, repair failed plan sections, and return a revised tag plan with critique history.",
  },
  {
    name: "Submit review decisions",
    method: "POST",
    endpoint: "/api/review/decisions",
    purpose: "Store human decisions before the approved tag plan is written into the PDF.",
  },
  {
    name: "Write PDF tags",
    method: "POST",
    endpoint: "/api/pdf/tag",
    purpose: "Apply the approved tag plan to a working copy of the PDF through the PDF tagging adapter.",
  },
  {
    name: "Validate output",
    method: "POST",
    endpoint: "/api/pdf/validate",
    purpose: "Run automated checks and return machine-detectable issues plus review-needed warnings.",
  },
  {
    name: "Export package",
    method: "GET",
    endpoint: "/api/pdf/export/:jobId",
    purpose: "Return the tagged PDF plus JSON reports for audit and repair history.",
  },
];

const fallbackTagTree = [
  { id: "sample-document", tag: "Document", label: "Uploaded PDF", confidence: 0.97 },
  { id: "sample-h1", tag: "H1", label: "Course Accessibility Policy", confidence: 0.94 },
  { id: "sample-p", tag: "P", label: "This document explains...", confidence: 0.91 },
  { id: "sample-h2", tag: "H2", label: "Requesting accommodations", confidence: 0.88 },
  { id: "sample-list", tag: "L", label: "Three-step request process", confidence: 0.83 },
  { id: "sample-figure", tag: "Figure", label: "Campus support diagram", confidence: 0.78 },
  { id: "sample-table", tag: "Table", label: "Office contact table", confidence: 0.72 },
  { id: "sample-artifact", tag: "Artifact", label: "Decorative footer line", confidence: 0.96 },
];

const fallbackReviewItems = [
  {
    id: "sample-reading-order",
    type: "Reading order",
    severity: "High",
    item: "Two-column page may read across columns instead of down the left column first.",
    action: "Review page 2 reading order before export.",
  },
  {
    id: "sample-alt-text",
    type: "Alt text",
    severity: "Medium",
    item: "Figure detected without meaningful alt text.",
    action: "Accept generated alt text or mark decorative.",
  },
  {
    id: "sample-table-headers",
    type: "Table headers",
    severity: "Medium",
    item: "Table appears to have row and column headers, but header scope is uncertain.",
    action: "Confirm header relationships.",
  },
  {
    id: "sample-artifacts",
    type: "Artifacts",
    severity: "Low",
    item: "Page numbers and footer rules were marked as artifacts.",
    action: "Spot-check that no meaningful content was hidden.",
  },
];

const adapterExample = `// Backend adapter shape for the real PDF tagging layer
export async function writePdfTags({ pdfFile, tagPlan, reviewDecisions }) {
  // 1. Open the PDF with the chosen backend PDF library or service.
  // 2. Apply the approved structure tree.
  // 3. Mark decorative content as artifacts.
  // 4. Attach approved alt text to figures.
  // 5. Apply approved table header relationships.
  // 6. Save a tagged working copy.
  // 7. Return the tagged PDF URL and repair log.

  return {
    jobId: "job_123",
    taggedPdfUrl: "/api/pdf/export/job_123",
    repairLogUrl: "/api/pdf/report/job_123",
  };
}`;

const localAiExample = `// Local AI call shape, for example Ollama or LM Studio
export async function runLocalAgent({ modelProvider, model, systemPrompt, userPayload }) {
  const response = await fetch("/api/ai/local-chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ modelProvider, model, systemPrompt, userPayload }),
  });

  if (!response.ok) throw new Error("Agent model call failed");
  return response.json();
}`;

const repairLoopExample = `// Backend orchestration shape for AI + deterministic repair
export async function runAgentRepairLoop({ jobId, analysisReport, agents, modelProvider, activeModel }) {
  const evidence = runDeterministicAnalysis(analysisReport);
  let tagPlan = await askSpecialistAgents({ evidence, agents, modelProvider, activeModel });
  const critiqueHistory = [];

  for (let pass = 1; pass <= 3; pass += 1) {
    const agentCritiques = await crossCheckAgents({ tagPlan, evidence, agents });
    const ruleFailures = runDeterministicChecks({ tagPlan, evidence });

    critiqueHistory.push({ pass, agentCritiques, ruleFailures });

    if (ruleFailures.blockers.length === 0 && agentCritiques.blockers.length === 0) break;

    tagPlan = await repairFailedSectionsOnly({
      tagPlan,
      evidence,
      agentCritiques,
      ruleFailures,
    });
  }

  return {
    jobId,
    tagPlan,
    critiqueHistory,
    reviewItems: collectHumanReviewItems({ tagPlan, critiqueHistory }),
  };
}`;

function confidenceClass(value) {
  if (value >= 0.9) return "bg-emerald-100 text-emerald-800 border-emerald-200";
  if (value >= 0.8) return "bg-amber-100 text-amber-800 border-amber-200";
  return "bg-rose-100 text-rose-800 border-rose-200";
}

function pipelineState(index, workflowStep) {
  const currentIndex = workflowIndex[workflowStep] ?? 0;
  if (workflowStep === "failed" && index === currentIndex) return "failed";
  if (index < currentIndex) return "done";
  if (index === currentIndex) return "active";
  return "waiting";
}

function normalizeTagTree(tagPlan) {
  if (!tagPlan) return fallbackTagTree;
  if (Array.isArray(tagPlan)) return tagPlan;
  if (Array.isArray(tagPlan.tagTree)) return tagPlan.tagTree;
  if (Array.isArray(tagPlan.tags)) return tagPlan.tags;
  if (Array.isArray(tagPlan.structureTree)) return tagPlan.structureTree;
  return fallbackTagTree;
}

function normalizeReviewItems(tagPlan, validationReport) {
  if (validationReport?.reviewItems?.length) return validationReport.reviewItems;
  if (validationReport?.issues?.length) return validationReport.issues;
  if (tagPlan?.reviewItems?.length) return tagPlan.reviewItems;
  if (tagPlan?.issues?.length) return tagPlan.issues;
  return fallbackReviewItems;
}

function getItemId(item, index) {
  return item.id || item.issueId || item.nodeId || `${item.type || "review"}-${index}`;
}

function getTagLabel(node) {
  return node.label || node.text || node.title || node.description || "Untitled node";
}

function getTagName(node) {
  return node.tag || node.type || node.role || "Tag";
}

function getConfidence(node) {
  const raw = node.confidence ?? node.score ?? 0.5;
  return typeof raw === "number" ? raw : Number(raw) || 0.5;
}

const draftSelfTests = [
  {
    name: "pipelineState marks previous steps complete",
    run: () => pipelineState(0, "reviewNeeded") === "done",
  },
  {
    name: "pipelineState marks the active review step",
    run: () => pipelineState(4, "reviewNeeded") === "active",
  },
  {
    name: "normalizeTagTree reads tagPlan.tagTree",
    run: () => normalizeTagTree({ tagTree: [{ id: "x", tag: "H1" }] })[0].tag === "H1",
  },
  {
    name: "normalizeTagTree falls back safely",
    run: () => normalizeTagTree(null) === fallbackTagTree,
  },
  {
    name: "normalizeReviewItems prefers validation review items",
    run: () => normalizeReviewItems({ reviewItems: [{ id: "tag" }] }, { reviewItems: [{ id: "validation" }] })[0].id === "validation",
  },
  {
    name: "getConfidence accepts numeric strings",
    run: () => getConfidence({ score: "0.82" }) === 0.82,
  },
  {
    name: "getItemId builds a fallback identifier",
    run: () => getItemId({ type: "Alt text" }, 2) === "Alt text-2",
  },
];

function runDraftSelfTests() {
  return draftSelfTests.map((test) => {
    try {
      return {
        name: test.name,
        passed: Boolean(test.run()),
      };
    } catch (caughtError) {
      return {
        name: test.name,
        passed: false,
        error: caughtError instanceof Error ? caughtError.message : "Unknown test failure",
      };
    }
  });
}

export default function MultiAgentPdfTaggerApp() {
  const [pdfFile, setPdfFile] = useState(null);
  const [fileName, setFileName] = useState("");
  const [workflowStep, setWorkflowStep] = useState("idle");
  const [loadingStep, setLoadingStep] = useState("");
  const [error, setError] = useState("");

  const [jobId, setJobId] = useState("");
  const [analysisReport, setAnalysisReport] = useState(null);
  const [tagPlan, setTagPlan] = useState(null);
  const [reviewDecisions, setReviewDecisions] = useState({});
  const [reviewed, setReviewed] = useState(false);
  const [validationReport, setValidationReport] = useState(null);
  const [taggedPdfUrl, setTaggedPdfUrl] = useState("");
  const [critiqueHistory, setCritiqueHistory] = useState([]);

  const [selectedAgent, setSelectedAgent] = useState(agents[0]);
  const [aiEnabled, setAiEnabled] = useState(true);
  const [taggingAdapterConnected, setTaggingAdapterConnected] = useState(false);
  const [backendBaseUrl, setBackendBaseUrl] = useState("http://localhost:3000");
  const [modelProvider, setModelProvider] = useState("Ollama / local model server");
  const [activeModel, setActiveModel] = useState("llama3.2:latest");
  const [repairPassLimit, setRepairPassLimit] = useState(3);

  const displayTagTree = useMemo(() => normalizeTagTree(tagPlan), [tagPlan]);
  const reviewItems = useMemo(() => normalizeReviewItems(tagPlan, validationReport), [tagPlan, validationReport]);
  const selfTestResults = useMemo(() => runDraftSelfTests(), []);
  const selfTestsPassed = selfTestResults.every((test) => test.passed);

  const allReviewItemsDecided = reviewItems.length > 0 && reviewItems.every((item, index) => reviewDecisions[getItemId(item, index)]?.decision);
  const canRunAgents = Boolean(pdfFile && aiEnabled && !loadingStep);
  const canWriteTags = Boolean(taggingAdapterConnected && jobId && tagPlan && reviewed && !loadingStep);
  const readyToExport = Boolean(taggedPdfUrl && workflowStep === "readyToExport" && !loadingStep);

  const agentStates = useMemo(() => {
    const agentWorkStarted = ["agentsRunning", "repairing", "reviewNeeded", "tagging", "validating", "readyToExport"].includes(workflowStep);
    const agentWorkComplete = ["reviewNeeded", "tagging", "validating", "readyToExport"].includes(workflowStep);

    return agents.map((agent, index) => ({
      ...agent,
      state: agentWorkComplete ? "Complete" : workflowStep === "agentsRunning" && index === 0 ? "Working" : agentWorkStarted ? "Waiting" : pdfFile ? "Ready" : "Waiting",
    }));
  }, [pdfFile, workflowStep]);

  function endpointUrl(endpoint) {
    const base = backendBaseUrl.replace(/\/$/, "");
    return `${base}${endpoint}`;
  }

  async function requestJson(endpoint, options = {}) {
    const response = await fetch(endpointUrl(endpoint), options);
    if (!response.ok) {
      const message = await response.text().catch(() => "");
      throw new Error(`${options.method || "GET"} ${endpoint} failed (${response.status})${message ? `: ${message.slice(0, 180)}` : ""}`);
    }

    const contentType = response.headers.get("content-type") || "";
    if (contentType.includes("application/json")) return response.json();
    return {};
  }

  function clearWorkflowOutputs() {
    setJobId("");
    setAnalysisReport(null);
    setTagPlan(null);
    setValidationReport(null);
    setTaggedPdfUrl("");
    setCritiqueHistory([]);
    setReviewDecisions({});
    setReviewed(false);
  }

  function handleUpload(event) {
    const file = event.target.files?.[0];
    if (!file) return;

    setPdfFile(file);
    setFileName(file.name);
    setWorkflowStep("uploaded");
    setError("");
    clearWorkflowOutputs();
  }

  async function checkTaggingAdapterHealth() {
    setError("");
    setLoadingStep("Checking PDF tagging adapter");

    try {
      const data = await requestJson("/api/pdf/tag/health");
      const available = Boolean(data.ok ?? data.available ?? data.connected ?? data.status === "ok");
      setTaggingAdapterConnected(available);

      if (!available) {
        throw new Error("PDF tagging adapter health check responded, but did not report an available adapter.");
      }
    } catch (caughtError) {
      setTaggingAdapterConnected(false);
      setError(caughtError instanceof Error ? caughtError.message : "PDF tagging adapter health check failed.");
    } finally {
      setLoadingStep("");
    }
  }

  async function uploadAndAnalyzePdf() {
    if (!pdfFile) throw new Error("Choose a PDF before analysis.");

    setWorkflowStep("analyzing");
    setLoadingStep("Analyzing PDF");

    const formData = new FormData();
    formData.append("file", pdfFile);

    const data = await requestJson("/api/pdf/analyze", {
      method: "POST",
      body: formData,
    });

    if (!data.jobId) {
      throw new Error("PDF analysis response must include jobId.");
    }

    const nextAnalysisReport = data.analysisReport || data.report || data;
    setJobId(data.jobId);
    setAnalysisReport(nextAnalysisReport);

    return {
      jobId: data.jobId,
      analysisReport: nextAnalysisReport,
    };
  }

  async function runAiAgents() {
    if (!pdfFile) {
      setError("Choose a PDF before running AI agents.");
      return;
    }

    if (!aiEnabled) {
      setError("AI agents are disabled.");
      return;
    }

    setError("");

    try {
      const analysis = jobId && analysisReport ? { jobId, analysisReport } : await uploadAndAnalyzePdf();

      setWorkflowStep("agentsRunning");
      setLoadingStep("Running AI cross-check and repair loop");

      const payload = {
        jobId: analysis.jobId,
        modelProvider,
        activeModel,
        repairPassLimit,
        collaborationPhases,
        deterministicChecks,
        crossCheckMatrix,
        agents: agents.map((agent) => ({
          name: agent.name,
          modelRole: agent.modelRole,
          endpoint: agent.endpoint,
          input: agent.input,
          output: agent.output,
        })),
        analysisReport: analysis.analysisReport,
      };

      const data = await requestJson("/api/agents/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const nextTagPlan = data.tagPlan || data.plan || data;
      setTagPlan(nextTagPlan);
      setCritiqueHistory(data.critiqueHistory || data.repairHistory || []);
      setValidationReport(data.validationReport || data.preflightReport || null);
      setReviewDecisions({});
      setReviewed(false);
      setWorkflowStep(data.needsRepair ? "repairing" : "reviewNeeded");
    } catch (caughtError) {
      setWorkflowStep("failed");
      setError(caughtError instanceof Error ? caughtError.message : "AI agent workflow failed.");
    } finally {
      setLoadingStep("");
    }
  }

  function setReviewDecision(itemId, decision) {
    setReviewDecisions((current) => ({
      ...current,
      [itemId]: {
        ...(current[itemId] || {}),
        decision,
      },
    }));
    setReviewed(false);
  }

  function setReviewNote(itemId, note) {
    setReviewDecisions((current) => ({
      ...current,
      [itemId]: {
        ...(current[itemId] || {}),
        note,
      },
    }));
    setReviewed(false);
  }

  async function submitReviewDecisions() {
    if (!jobId) throw new Error("Cannot submit review decisions before a job exists.");
    if (!allReviewItemsDecided) throw new Error("Every review item needs a decision before submission.");

    setLoadingStep("Submitting review decisions");

    await requestJson("/api/review/decisions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jobId,
        reviewDecisions,
      }),
    });

    setReviewed(true);
  }

  async function handleSubmitReviewDecisions() {
    setError("");

    try {
      await submitReviewDecisions();
    } catch (caughtError) {
      setError(caughtError instanceof Error ? caughtError.message : "Review decision submission failed.");
    } finally {
      setLoadingStep("");
    }
  }

  async function writePdfTags() {
    if (!taggingAdapterConnected) throw new Error("Connect the PDF tagging adapter before writing tags.");
    if (!jobId || !tagPlan) throw new Error("Run AI agents before writing tags.");
    if (!reviewed) await submitReviewDecisions();

    setWorkflowStep("tagging");
    setLoadingStep("Writing PDF tags");

    const data = await requestJson("/api/pdf/tag", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jobId,
        tagPlan,
        reviewDecisions,
      }),
    });

    if (data.taggedPdfUrl) setTaggedPdfUrl(data.taggedPdfUrl);
    if (data.validationReport) setValidationReport(data.validationReport);

    return data;
  }

  async function validateTaggedPdf(nextTaggedPdfUrl = "") {
    if (!jobId) throw new Error("Cannot validate before a job exists.");

    setWorkflowStep("validating");
    setLoadingStep("Validating tagged PDF");

    const data = await requestJson("/api/pdf/validate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        jobId,
        taggedPdfUrl: nextTaggedPdfUrl || taggedPdfUrl,
      }),
    });

    setValidationReport(data.validationReport || data.report || data);

    const finalTaggedPdfUrl = data.taggedPdfUrl || nextTaggedPdfUrl || taggedPdfUrl;
    if (finalTaggedPdfUrl) {
      setTaggedPdfUrl(finalTaggedPdfUrl);
      setWorkflowStep("readyToExport");
    }

    return data;
  }

  async function writeAndValidatePdf() {
    setError("");

    try {
      const tagWriteResult = await writePdfTags();
      await validateTaggedPdf(tagWriteResult.taggedPdfUrl || "");
    } catch (caughtError) {
      setWorkflowStep("failed");
      setError(caughtError instanceof Error ? caughtError.message : "PDF tagging or validation failed.");
    } finally {
      setLoadingStep("");
    }
  }

  function exportTaggedPdf() {
    if (!jobId) {
      setError("Cannot export before a job exists.");
      return;
    }

    const exportUrl = taggedPdfUrl || endpointUrl(`/api/pdf/export/${jobId}`);
    window.open(exportUrl, "_blank", "noopener,noreferrer");
  }

  function reset() {
    setPdfFile(null);
    setFileName("");
    setWorkflowStep("idle");
    setLoadingStep("");
    setError("");
    clearWorkflowOutputs();
    setSelectedAgent(agents[0]);
  }

  return (
    <div className="min-h-screen bg-slate-50 text-slate-950">
      <div className="mx-auto max-w-7xl px-6 py-8">
        <header className="mb-8 grid gap-6 lg:grid-cols-[1.25fr_0.75fr] lg:items-end">
          <div>
            <div className="mb-3 inline-flex items-center gap-2 rounded-full border border-slate-200 bg-white px-3 py-1 text-sm text-slate-600 shadow-sm">
              <Bot className="h-4 w-4" />
              Multi-agent AI PDF tagging workspace
            </div>
            <h1 className="text-4xl font-semibold tracking-tight md:text-5xl">Tag a PDF with AI agents and a PDF tagging adapter</h1>
            <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-600">
              Upload a PDF, route it through specialist AI agents, review the proposed tag plan, then send the approved plan to a backend PDF tagging adapter.
            </p>
          </div>
          <Card className="rounded-2xl border-slate-200 shadow-sm">
            <CardContent className="p-5">
              <div className="flex items-start gap-3">
                <ShieldCheck className="mt-1 h-5 w-5" />
                <div>
                  <h2 className="font-semibold">Guardrail</h2>
                  <p className="mt-1 text-sm leading-6 text-slate-600">
                    AI agents draft, critique, and repair the structure. Deterministic code checks their claims. Human review approves meaning-sensitive decisions. The PDF tagging adapter writes the approved tags into the PDF.
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>
        </header>

        <div className="mb-6 rounded-2xl border border-slate-200 bg-white p-4 shadow-sm" role="status" aria-live="polite">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <div>
              <p className="font-semibold">Workflow status: {workflowStep}</p>
              <p className="mt-1 text-sm text-slate-600">{loadingStep || "Ready for the next action."}</p>
            </div>
            {error && (
              <div className="max-w-2xl rounded-xl border border-rose-200 bg-rose-50 px-3 py-2 text-sm text-rose-800">
                {error}
              </div>
            )}
          </div>
        </div>

        <main className="grid gap-6 lg:grid-cols-[0.9fr_1.35fr_0.95fr]">
          <section className="space-y-6">
            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><Upload className="h-5 w-5" />PDF intake</h2>
                <label htmlFor="pdf-upload" className="mt-4 flex cursor-pointer flex-col items-center justify-center rounded-2xl border border-dashed border-slate-300 bg-white px-4 py-8 text-center transition hover:bg-slate-100">
                  <FileText className="mb-3 h-9 w-9 text-slate-500" />
                  <span className="font-medium">Choose a PDF</span>
                  <span className="mt-1 text-sm text-slate-500">The frontend stores the file; the backend handles real extraction and tagging.</span>
                  <input id="pdf-upload" type="file" accept="application/pdf" className="hidden" onChange={handleUpload} />
                </label>
                <div className="mt-4 rounded-xl bg-slate-100 p-3 text-sm"><span className="font-medium">Current file: </span>{fileName || "No file selected"}</div>
                <div className="mt-4 flex flex-wrap gap-2">
                  <Button onClick={runAiAgents} disabled={!canRunAgents} className="rounded-xl">
                    {loadingStep ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : <BrainCircuit className="mr-2 h-4 w-4" />}
                    Run AI repair loop
                  </Button>
                  <Button variant="outline" onClick={reset} className="rounded-xl">Reset</Button>
                </div>
              </CardContent>
            </Card>

            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><BrainCircuit className="h-5 w-5" />AI model wiring</h2>
                <div className="mt-4 space-y-3">
                  <div>
                    <label htmlFor="model-provider" className="block text-sm font-medium text-slate-700">Model provider</label>
                    <input id="model-provider" value={modelProvider} onChange={(event) => setModelProvider(event.target.value)} className="mt-1 w-full rounded-xl border border-slate-200 bg-white px-3 py-2 text-sm outline-none focus:border-slate-500" />
                  </div>
                  <div>
                    <label htmlFor="active-model" className="block text-sm font-medium text-slate-700">Active model</label>
                    <input id="active-model" value={activeModel} onChange={(event) => setActiveModel(event.target.value)} className="mt-1 w-full rounded-xl border border-slate-200 bg-white px-3 py-2 text-sm outline-none focus:border-slate-500" />
                  </div>
                  <div>
                    <label htmlFor="repair-pass-limit" className="block text-sm font-medium text-slate-700">AI repair pass limit</label>
                    <input id="repair-pass-limit" type="number" min="1" max="5" value={repairPassLimit} onChange={(event) => setRepairPassLimit(Number(event.target.value) || 1)} className="mt-1 w-full rounded-xl border border-slate-200 bg-white px-3 py-2 text-sm outline-none focus:border-slate-500" />
                  </div>
                  <div className="flex items-center justify-between rounded-xl bg-slate-100 px-3 py-2 text-sm">
                    <span>Enable AI agents</span>
                    <button type="button" aria-pressed={aiEnabled} onClick={() => setAiEnabled(!aiEnabled)} className={`rounded-full px-3 py-1 text-xs font-semibold ${aiEnabled ? "bg-emerald-100 text-emerald-800" : "bg-slate-200 text-slate-600"}`}>{aiEnabled ? "On" : "Off"}</button>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><GitBranch className="h-5 w-5" />Pipeline</h2>
                <div className="mt-4 space-y-3">
                  {pipeline.map((step, index) => {
                    const state = pipelineState(index, workflowStep);
                    return (
                      <div key={step} className="flex items-center gap-3">
                        <div className={`flex h-7 w-7 items-center justify-center rounded-full border text-xs font-semibold ${state === "done" ? "border-emerald-300 bg-emerald-100 text-emerald-800" : state === "active" ? "border-slate-900 bg-slate-900 text-white" : state === "failed" ? "border-rose-300 bg-rose-100 text-rose-800" : "border-slate-200 bg-white text-slate-400"}`}>
                          {state === "done" ? <CheckCircle2 className="h-4 w-4" /> : index + 1}
                        </div>
                        <span className={state === "waiting" ? "text-slate-400" : "text-slate-800"}>{step}</span>
                      </div>
                    );
                  })}
                </div>
              </CardContent>
            </Card>
          </section>

          <section className="space-y-6">
            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><Bot className="h-5 w-5" />AI agent team</h2>
                <div className="mt-4 grid gap-3 md:grid-cols-2">
                  {agentStates.map((agent) => (
                    <motion.button key={agent.name} whileHover={{ y: -2 }} onClick={() => setSelectedAgent(agent)} className={`rounded-2xl border bg-white p-4 text-left shadow-sm transition ${selectedAgent.name === agent.name ? "border-slate-900" : "border-slate-200 hover:border-slate-300"}`}>
                      <div className="flex items-start justify-between gap-3">
                        <h3 className="font-semibold">{agent.name}</h3>
                        <span className={`rounded-full px-2 py-1 text-xs font-medium ${agent.state === "Complete" ? "bg-emerald-100 text-emerald-800" : agent.state === "Working" ? "bg-slate-900 text-white" : "bg-slate-100 text-slate-500"}`}>{agent.state}</span>
                      </div>
                      <p className="mt-2 text-sm leading-6 text-slate-600">{agent.role}</p>
                      <div className="mt-3 rounded-xl bg-slate-100 p-2 text-xs text-slate-600">
                        <div><span className="font-semibold">Model role:</span> {agent.modelRole}</div>
                        <div className="mt-1"><span className="font-semibold">Endpoint:</span> {agent.endpoint}</div>
                      </div>
                    </motion.button>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><Workflow className="h-5 w-5" />Cross-check and repair loop</h2>
                <div className="mt-4 space-y-3">
                  {collaborationPhases.map((phase, index) => (
                    <div key={phase.name} className="rounded-2xl border border-slate-200 bg-white p-3">
                      <div className="flex items-center gap-2">
                        <span className="flex h-6 w-6 items-center justify-center rounded-full bg-slate-100 text-xs font-semibold text-slate-700">{index + 1}</span>
                        <span className="font-medium">{phase.name}</span>
                      </div>
                      <p className="mt-2 text-sm leading-6 text-slate-600">{phase.purpose}</p>
                    </div>
                  ))}
                </div>
                {critiqueHistory.length > 0 && (
                  <div className="mt-4 rounded-2xl bg-slate-100 p-3 text-sm text-slate-700">
                    Critique history received: {critiqueHistory.length} repair pass{critiqueHistory.length === 1 ? "" : "es"}.
                  </div>
                )}
              </CardContent>
            </Card>

            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><Eye className="h-5 w-5" />Proposed tag tree</h2>
                <p className="mt-2 text-sm leading-6 text-slate-600">
                  {tagPlan ? "Showing the tag plan returned by the AI repair loop." : "Showing sample structure until the backend returns a tag plan."}
                </p>
                <div className="mt-4 overflow-hidden rounded-2xl border border-slate-200 bg-white">
                  {displayTagTree.map((node, index) => {
                    const confidence = getConfidence(node);
                    return (
                      <div key={node.id || `${getTagName(node)}-${index}`} className="grid grid-cols-[90px_1fr_auto] items-center gap-3 border-b border-slate-100 px-4 py-3 last:border-b-0">
                        <span className="rounded-lg bg-slate-100 px-2 py-1 text-center font-mono text-sm font-semibold text-slate-700">{getTagName(node)}</span>
                        <span className="truncate text-sm text-slate-700" style={{ paddingLeft: `${Math.min(index, 4) * 10}px` }}>{getTagLabel(node)}</span>
                        <span className={`rounded-full border px-2 py-1 text-xs font-semibold ${confidenceClass(confidence)}`}>{Math.round(confidence * 100)}%</span>
                      </div>
                    );
                  })}
                </div>
              </CardContent>
            </Card>

            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><CheckCircle2 className="h-5 w-5" />Deterministic checks</h2>
                <div className="mt-4 space-y-2">
                  {deterministicChecks.map((check) => (
                    <div key={check} className="flex gap-2 rounded-xl bg-slate-100 p-3 text-sm leading-6 text-slate-700">
                      <CheckCircle2 className="mt-1 h-4 w-4 shrink-0" />
                      <span>{check}</span>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><PlugZap className="h-5 w-5" />Backend hooks</h2>
                <div className="mt-4 space-y-3">
                  {backendHooks.map((hook) => (
                    <div key={hook.endpoint} className="rounded-2xl border border-slate-200 bg-white p-3">
                      <div className="flex flex-wrap items-center justify-between gap-2">
                        <span className="font-medium">{hook.name}</span>
                        <span className="rounded-full bg-slate-100 px-2 py-1 font-mono text-xs text-slate-600">{hook.method} {hook.endpoint}</span>
                      </div>
                      <p className="mt-2 text-sm leading-6 text-slate-600">{hook.purpose}</p>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </section>

          <section className="space-y-6">
            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><PlugZap className="h-5 w-5" />PDF tagging adapter</h2>
                <div className="mt-4 space-y-3">
                  <div>
                    <label htmlFor="backend-base-url" className="block text-sm font-medium text-slate-700">Backend base URL</label>
                    <input id="backend-base-url" value={backendBaseUrl} onChange={(event) => setBackendBaseUrl(event.target.value)} className="mt-1 w-full rounded-xl border border-slate-200 bg-white px-3 py-2 text-sm outline-none focus:border-slate-500" />
                  </div>
                  <button type="button" aria-pressed={taggingAdapterConnected} onClick={checkTaggingAdapterHealth} disabled={Boolean(loadingStep)} className={`flex w-full items-center justify-center gap-2 rounded-xl px-3 py-2 text-sm font-semibold ${taggingAdapterConnected ? "bg-emerald-100 text-emerald-800" : "bg-slate-900 text-white"}`}>
                    {loadingStep === "Checking PDF tagging adapter" ? <RefreshCw className="h-4 w-4 animate-spin" /> : <PlugZap className="h-4 w-4" />}
                    {taggingAdapterConnected ? "PDF tagging adapter connected" : "Check PDF tagging adapter"}
                  </button>
                  <p className="text-sm leading-6 text-slate-600">
                    This health check replaces the fake connection toggle. The backend must respond from <span className="font-mono">/api/pdf/tag/health</span> before the app can write approved tags.
                  </p>
                </div>
              </CardContent>
            </Card>

            <Card className="rounded-2xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <h2 className="flex items-center gap-2 text-xl font-semibold"><Bot className="h-5 w-5" />Selected agent</h2>
                <div