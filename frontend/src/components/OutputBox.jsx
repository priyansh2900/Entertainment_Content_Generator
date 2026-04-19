function OutputBox({ title, content, isError = false }) {
  if (!content) return null;

  return (
    <div className={`output-box ${isError ? "error-box" : ""}`}>
      <h2>{title}</h2>
      <pre>{content}</pre>
    </div>
  );
}

export default OutputBox;