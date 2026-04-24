const API_TEAM_URL = "http://localhost:5000/api/team";

const tableBody = document.getElementById("team-table-body");
const backendStatus = document.getElementById("backend-status");
const message = document.getElementById("message");

function setBackendStatus(text, backgroundColor, textColor = "#111827") {
  backendStatus.textContent = text;
  backendStatus.style.backgroundColor = backgroundColor;
  backendStatus.style.color = textColor;
}

function clearTable() {
  tableBody.innerHTML = "";
}

function renderMembers(members) {
  clearTable();

  members.forEach((member) => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${member.nombre ?? ""}</td>
      <td>${member.apellido ?? ""}</td>
      <td>${member.legajo ?? ""}</td>
      <td>${member.feature ?? ""}</td>
      <td>${member.servicio ?? ""}</td>
      <td>${member.estado ?? ""}</td>
    `;

    tableBody.appendChild(row);
  });
}

async function loadTeam() {
  setBackendStatus("Verificando estado del backend...", "#e5e7eb");
  message.textContent = "";

  try {
    const response = await fetch(API_TEAM_URL);

    if (!response.ok) {
      throw new Error(`Error HTTP ${response.status}`);
    }

    const members = await response.json();

    setBackendStatus("Backend conectado", "#dcfce7", "#166534");

    if (!Array.isArray(members) || members.length === 0) {
      clearTable();
      message.textContent = "No hay integrantes para mostrar.";
      return;
    }

    renderMembers(members);
  } catch (error) {
    clearTable();
    setBackendStatus("Backend no disponible", "#fee2e2", "#991b1b");
    message.textContent = "No se pudieron cargar los datos del equipo.";
    console.error("Error al obtener integrantes:", error);
  }
}

loadTeam();