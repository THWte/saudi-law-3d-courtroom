// Dashboard Logic

class DashboardManager {
    constructor() {
        this.currentMode = 'ai-assisted';
        this.currentPage = 'overview';
        this.initializeEventListeners();
        this.loadInitialData();
    }

    initializeEventListeners() {
        // Navigation Items
        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                const pageName = item.dataset.page + '-page';
                this.showPage(pageName);
                this.updateNavigation(item);
            });
        });

        // Mode Cards
        document.querySelectorAll('.mode-card').forEach(card => {
            card.addEventListener('click', () => this.selectMode(card.dataset.mode));
        });

        // Form Submission
        const caseForm = document.getElementById('new-case-form');
        if (caseForm) {
            caseForm.addEventListener('submit', (e) => this.handleCaseSubmission(e));
        }

        // File Upload
        const fileUpload = document.querySelector('.file-upload');
        if (fileUpload) {
            fileUpload.addEventListener('click', () => {
                document.getElementById('case-files').click();
            });
            fileUpload.addEventListener('dragover', (e) => {
                e.preventDefault();
                fileUpload.style.background = 'rgba(110, 201, 255, 0.15)';
            });
            fileUpload.addEventListener('drop', (e) => {
                e.preventDefault();
                this.handleFileUpload(e.dataTransfer.files);
            });
        }
    }

    showPage(pageName) {
        // Hide all pages
        document.querySelectorAll('.page').forEach(page => {
            page.classList.remove('active');
        });

        // Show selected page
        const pageElement = document.getElementById(pageName);
        if (pageElement) {
            pageElement.classList.add('active');
            this.currentPage = pageName;
        }
    }

    updateNavigation(activeItem) {
        document.querySelectorAll('.nav-item').forEach(item => {
            item.classList.remove('active');
        });
        activeItem.classList.add('active');
    }

    selectMode(mode) {
        this.currentMode = mode;
        console.log(`Mode switched to: ${mode}`);

        // Update UI
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-mode="${mode}"] .mode-btn`).classList.add('active');

        // Send to backend
        this.sendToAPI('/api/set-mode', { mode: mode });
    }

    handleCaseSubmission(e) {
        e.preventDefault();

        const caseData = {
            description: document.getElementById('case-description')?.value || '',
            plaintiff: document.getElementById('plaintiff-name')?.value || '',
            defendant: document.getElementById('defendant-name')?.value || '',
            caseType: document.getElementById('case-type')?.value || '',
            hasEvidence: document.querySelector('input[name="has-evidence"]')?.checked || false,
            hasWitnesses: document.querySelector('input[name="has-witnesses"]')?.checked || false,
            urgent: document.querySelector('input[name="urgent"]')?.checked || false
        };

        // Send to backend for analysis
        this.sendToAPI('/api/analyze-case', { case: caseData, mode: this.currentMode })
            .then(response => {
                this.displayAnalysisResults(response);
                this.showPage('analysis-page');
            })
            .catch(error => console.error('Error:', error));
    }

    handleFileUpload(files) {
        const formData = new FormData();
        for (let file of files) {
            formData.append('files', file);
        }

        this.sendToAPI('/api/upload-files', formData, true)
            .then(response => {
                console.log('Files uploaded:', response);
                this.displayUploadedFiles(response);
            })
            .catch(error => console.error('Upload error:', error));
    }

    displayAnalysisResults(data) {
        const resultsDiv = document.getElementById('analysis-results');
        if (resultsDiv) {
            resultsDiv.innerHTML = `
                <div class="analysis-card">
                    <h3>نوع القضية: ${data.case_type || 'غير محدد'}</h3>
                    <p><strong>الأطراف:</strong> ${data.parties?.join(', ') || 'غير محددة'}</p>
                    <p><strong>الحقائق الأساسية:</strong> ${data.facts || 'لم يتم استخراج الحقائق'}</p>
                    <p><strong>المخاطر:</strong> ${data.risks?.join(', ') || 'لا توجد'}</p>
                    <p><strong>القوانين المنطبقة:</strong> ${data.laws?.join(', ') || 'لا توجد'}</p>
                </div>
            `;
        }
    }

    displayUploadedFiles(response) {
        console.log('Files processed:', response);
    }

    sendToAPI(endpoint, data, isFormData = false) {
        const options = {
            method: 'POST',
            headers: isFormData ? {} : { 'Content-Type': 'application/json' },
            body: isFormData ? data : JSON.stringify(data)
        };

        return fetch(endpoint, options)
            .then(response => response.json())
            .catch(error => {
                console.error('API Error:', error);
                return null;
            });
    }

    loadInitialData() {
        console.log('Dashboard initialized with mode:', this.currentMode);
    }
}

// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {
    new DashboardManager();
});
