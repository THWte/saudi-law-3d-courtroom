// Client-side API handler

class APIClient {
    constructor(baseURL = 'http://localhost:5000') {
        this.baseURL = baseURL;
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const defaultOptions = {
            headers: {
                'Content-Type': 'application/json'
            }
        };

        const finalOptions = { ...defaultOptions, ...options };

        try {
            const response = await fetch(url, finalOptions);
            if (!response.ok) {
                throw new Error(`API Error: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Request failed:', error);
            throw error;
        }
    }

    // Case Analysis
    async analyzeCase(caseData, mode = 'AI_ASSISTED') {
        return this.request('/api/analyze-case', {
            method: 'POST',
            body: JSON.stringify({ case: caseData, mode })
        });
    }

    // Strategy
    async getStrategy(caseId) {
        return this.request(`/api/strategy/${caseId}`);
    }

    // Courtroom Scene
    async getCourtroom() {
        return this.request('/api/courtroom-scene');
    }

    // Training
    async getTrainingScenarios() {
        return this.request('/api/training-scenarios');
    }

    // Statistics
    async getStatistics() {
        return this.request('/api/statistics');
    }

    // Set Mode
    async setMode(mode) {
        return this.request('/api/set-mode', {
            method: 'POST',
            body: JSON.stringify({ mode })
        });
    }

    // File Upload
    async uploadFiles(files) {
        const formData = new FormData();
        for (let file of files) {
            formData.append('files', file);
        }

        return this.request('/api/upload-files', {
            method: 'POST',
            body: formData,
            headers: {} // Let browser set the header for FormData
        });
    }
}

// Global instance
const api = new APIClient();
