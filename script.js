const API_URL = 'https://zenquotes.io/api/random';

async function fetchInspiration() {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();

    document.getElementById('quote').innerText = `"${data[0].q}"`;
    document.getElementById('author').innerText = `- ${data[0].a}`;
  } catch (error) {
    console.error("Error fetching quote:", error);
    document.getElementById('quote').innerText = "Could not load inspiration.";
  }
}

// Fetch a quote when the page loads
fetchInspiration();
