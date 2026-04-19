function Form({ formData, handleChange, handleGenerate, loading }) {
  return (
    <div className="form-box">
      <label htmlFor="topic">Topic</label>
      <textarea
        id="topic"
        name="topic"
        value={formData.topic}
        onChange={handleChange}
        placeholder="Enter your scene idea..."
        rows="5"
      />

      <label htmlFor="genre">Genre</label>
      <select
        id="genre"
        name="genre"
        value={formData.genre}
        onChange={handleChange}
      >
        <option value="Drama">Drama</option>
        <option value="Crime">Crime</option>
        <option value="Romance">Romance</option>
        <option value="Thriller">Thriller</option>
        <option value="Comedy">Comedy</option>
      </select>

      <label htmlFor="mood">Mood</label>
      <select
        id="mood"
        name="mood"
        value={formData.mood}
        onChange={handleChange}
      >
        <option value="Emotional">Emotional</option>
        <option value="Dark">Dark</option>
        <option value="Tense">Tense</option>
        <option value="Suspenseful">Suspenseful</option>
        <option value="Hopeful">Hopeful</option>
      </select>

      <label htmlFor="scene_length">Scene Length</label>
      <select
        id="scene_length"
        name="scene_length"
        value={formData.scene_length}
        onChange={handleChange}
      >
        <option value="Short">Short</option>
        <option value="Medium">Medium</option>
        <option value="Long">Long</option>
      </select>

      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate Scene"}
      </button>
    </div>
  );
}

export default Form;