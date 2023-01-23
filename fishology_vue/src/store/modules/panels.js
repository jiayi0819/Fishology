const state = {
  panels: {},
  // panelStatus: {
  //   showPanelCanvas: false,
  //   showCatalogue: false,
  //   showReadPanel: false,
  //   showWritePanel: false,
  //   writePanel: false,
  // },
};

const getters = {
  getPanels(state) {
    return state.panels;
  },
  // getPanelCanvasState: (state) => state.panelStatus.showPanelCanvas,
  // getReadPanelState: (state) => state.panelStatus.showReadPanel,
  // getCatalogueState: (state) => state.panelStatus.showCatalogue,
  // getWritePanelState: (state) => state.panelStatus.showWritePanel,
};

const mutations = {
  setPanel(state, modalName, modal) {
    state.panels[`${modalName}`] = modal;
  },

  // closeAllPanels(state) {
  //   Object.keys(state.panelStatus).forEach(
  //     (i) => (state.panelStatus[i] = false)
  //   );
  // },

  // changePanelCanvasState(state) {
  //   state.panelStatus.showPanelCanvas = !state.panelStatus.showPanelCanvas;
  // },

  // changeReadPanelState(state) {
  //   state.panelStatus.showReadPanel = !state.panelStatus.showReadPanel;
  // },
  // changeWritePanelState(state) {
  //   state.panelStatus.showWritePanel = !state.panelStatus.showWritePanel;
  // },
  // changeCatalogueState(state) {
  //   state.panelStatus.showCatalogue = !state.panelStatus.showCatalogue;
  // },
};

const actions = {
  // CLOSE ALL PANELS BEFORE OPEN ANOTHER

  initializePanels({ state, commit }) {
    state.panels["writeDiaryModal"] = new bootstrap.Modal(
      document.getElementById("writeDiaryModal")
    );

    state.panels["readDiaryModal"] = new bootstrap.Modal(
      document.getElementById("readDiaryModal")
    );

    state.panels["catalogueModal"] = new bootstrap.Modal(
      document.getElementById("catalogueModal")
    );

    state.panels["statisticsModal"] = new bootstrap.Modal(
      document.getElementById("statisticsModal")
    );

    state.panels["filterModal"] = new bootstrap.Modal(
      document.getElementById("filterModal")
    );

    state.panels["editAquariumModal"] = new bootstrap.Modal(
      document.getElementById("editAquariumModal")
    );

    for (const key in state.panels) {
      document
        .getElementById(key)
        .addEventListener("hidden.bs.modal", function (event) {
          state.modalOpened = false;
        });
    }
  },

  openModal({ state }, modalName) {
    if (!state.modalOpened) {
      state.panels[`${modalName}`].toggle();
      state.modalOpened = true;
    }
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
