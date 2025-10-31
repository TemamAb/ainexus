const ContinuousOptimizer = require('./continuous-optimizer');
const AutoProfitTransfer = require('./auto-transfer');
const PerformanceMonitor = require('../dashboard/performance');

class Phase2Orchestrator {
    constructor() {
        this.optimizer = new ContinuousOptimizer();
        this.profitTransfer = new AutoProfitTransfer();
        this.isRunning = false;
    }

    startPhase2() {
        console.log('íº€ STARTING PHASE 2: DASHBOARD + AUTO PROFIT + AI OPTIMIZATION');
        
        this.isRunning = true;
        
        // Start continuous AI optimization
        this.optimizer.startContinuousOptimization();
        
        // Start performance monitoring
        this.startPerformanceTracking();
        
        // Initialize auto profit transfer
        this.initializeProfitTransfer();
        
        console.log('âœ… PHASE 2 SYSTEMS: OPERATIONAL');
        console.log('í³Š Dashboard: http://localhost:3000/dashboard');
        console.log('í´– AI Optimization: CONTINUOUS');
        console.log('í²° Auto Profit Transfer: ACTIVE');
    }

    startPerformanceTracking() {
        setInterval(() => {
            // Simulate trade recording
            const profit = Math.random() * 1000 + 500;
            const success = Math.random() > 0.1;
            
            // this would record actual trades in production
            console.log(`í³ˆ Recorded trade: $${profit.toFixed(2)} - ${success ? 'SUCCESS' : 'FAILED'}`);
        }, 30000); // Every 30 seconds
    }

    initializeProfitTransfer() {
        setInterval(async () => {
            const status = this.profitTransfer.getTransferStatus();
            if (status.readyForTransfer) {
                await this.profitTransfer.transferProfits(status.accumulated);
            }
        }, 3600000); // Check every hour
    }
}

// Start Phase 2 if run directly
if (require.main === module) {
    const orchestrator = new Phase2Orchestrator();
    orchestrator.startPhase2();
}

module.exports = Phase2Orchestrator;
