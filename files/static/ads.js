/**
 * Ads Management System
 * Handles lazy loading of advertisements with Google AdSense compliance
 */

class AdsManager {
    constructor() {
        this.adsLoaded = false;
        this.adSlots = [];
        this.adConfig = {
            enabled: true,
            lazyLoad: true,
            delayMs: 2000  // Delay ad loading by 2 seconds
        };
    }

    /**
     * Initialize ads manager and register ad slots
     */
    init() {
        if (!this.adConfig.enabled) return;

        // Wait for DOM to be fully loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.setupAds());
        } else {
            this.setupAds();
        }
    }

    /**
     * Setup all ad slots on the page
     */
    setupAds() {
        const adSlots = document.querySelectorAll('[data-ad-slot]');
        
        if (adSlots.length === 0) return;

        adSlots.forEach((slot, index) => {
            const slotId = slot.getAttribute('data-ad-slot');
            const slotType = slot.getAttribute('data-ad-type') || 'display';
            
            this.adSlots.push({
                element: slot,
                id: slotId,
                type: slotType,
                loaded: false
            });

            // Add "Advertisement" label
            this.addAdLabel(slot);

            // Setup lazy loading
            if (this.adConfig.lazyLoad) {
                this.setupLazyLoad(slot, index);
            } else {
                this.loadAd(slot);
            }
        });

        // Fallback: Load all ads after delay
        if (this.adConfig.lazyLoad) {
            setTimeout(() => {
                this.loadAllVisibleAds();
            }, this.adConfig.delayMs);
        }
    }

    /**
     * Add "Advertisement" label above ad
     */
    addAdLabel(adElement) {
        const label = document.createElement('div');
        label.className = 'ad-label';
        label.textContent = '📢 Advertisement';
        adElement.insertBefore(label, adElement.firstChild);
    }

    /**
     * Setup lazy loading for ad with Intersection Observer
     */
    setupLazyLoad(adElement, index) {
        if (!('IntersectionObserver' in window)) {
            // Fallback for older browsers
            setTimeout(() => this.loadAd(adElement), this.adConfig.delayMs + (index * 500));
            return;
        }

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting && !entry.target.dataset.loaded) {
                    this.loadAd(entry.target);
                    entry.target.dataset.loaded = 'true';
                    observer.unobserve(entry.target);
                }
            });
        }, {
            rootMargin: '50px'  // Load ad when 50px below viewport
        });

        observer.observe(adElement);
    }

    /**
     * Load an individual ad
     */
    loadAd(adElement) {
        const slotId = adElement.getAttribute('data-ad-slot');
        const slotType = adElement.getAttribute('data-ad-type') || 'display';

        // Add placeholder for ads (will be replaced with real AdSense code)
        const placeholder = document.createElement('div');
        placeholder.className = 'ad-placeholder';
        placeholder.innerHTML = `
            <div class="ad-placeholder-content">
                <div class="ad-placeholder-icon">📺</div>
                <p>Google AdSense Advertisement</p>
                <small>Ad ID: ${slotId} (${slotType})</small>
            </div>
        `;

        adElement.appendChild(placeholder);

        // Mark as loaded
        adElement.dataset.loaded = 'true';
        this.adsLoaded = true;

        // Log for AdSense integration debugging
        console.log(`Ad loaded: ${slotId} (${slotType})`);
    }

    /**
     * Load all visible ads on page
     */
    loadAllVisibleAds() {
        this.adSlots.forEach((slot) => {
            if (!slot.loaded && slot.element.dataset.loaded !== 'true') {
                this.loadAd(slot.element);
                slot.loaded = true;
            }
        });
    }

    /**
     * Refresh ads (useful after AJAX content load)
     */
    refresh() {
        const newAdSlots = document.querySelectorAll('[data-ad-slot]:not([data-loaded="true"])');
        newAdSlots.forEach((slot) => {
            if (this.adConfig.lazyLoad) {
                this.setupLazyLoad(slot, 0);
            } else {
                this.loadAd(slot);
            }
        });
    }

    /**
     * Disable ads
     */
    disable() {
        this.adConfig.enabled = false;
        console.log('Ads disabled');
    }

    /**
     * Enable ads
     */
    enable() {
        this.adConfig.enabled = true;
        if (!this.adsLoaded) {
            this.init();
        }
        console.log('Ads enabled');
    }

    /**
     * Get ads statistics
     */
    getStats() {
        return {
            totalSlots: this.adSlots.length,
            loadedSlots: this.adSlots.filter(s => s.loaded).length,
            enabled: this.adConfig.enabled
        };
    }
}

// Initialize ads manager when DOM is ready
const adsManager = new AdsManager();

// Auto-initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => adsManager.init());
} else {
    adsManager.init();
}

// Export for external use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = adsManager;
}
