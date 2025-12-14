import streamlit as st

def add_custom_css():
    st.markdown("""
        <style>
        /* ============================================
           STUNTING GUARD - PREMIUM UI DESIGN SYSTEM
           ============================================ */
        
        /* 1. GOOGLE FONTS IMPORT */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        /* 2. ROOT VARIABLES - PREMIUM COLOR PALETTE */
        :root {
            --primary-50: #ECFDF5;
            --primary-100: #D1FAE5;
            --primary-200: #A7F3D0;
            --primary-300: #6EE7B7;
            --primary-400: #34D399;
            --primary-500: #10B981;
            --primary-600: #059669;
            --primary-700: #047857;
            --primary-800: #065F46;
            --primary-900: #064E3B;
            
            --accent-gradient: linear-gradient(135deg, #059669 0%, #10B981 50%, #34D399 100%);
            --accent-gradient-hover: linear-gradient(135deg, #047857 0%, #059669 50%, #10B981 100%);
            
            --glass-bg: rgba(255, 255, 255, 0.85);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            --shadow-green: 0 10px 30px -10px rgba(5, 150, 105, 0.4);
        }
        
        /* 3. GLOBAL FONT SETTING */
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        
        /* 4. MAIN CONTENT AREA */
        .main .block-container {
            padding: 2rem 3rem 3rem 3rem;
            max-width: 1200px;
        }

        /* 5. HEADINGS - PREMIUM TYPOGRAPHY */
        h1 {
            font-family: 'Inter', sans-serif !important;
            font-weight: 800 !important;
            font-size: 2.5rem !important;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.02em;
            margin-bottom: 0.5rem !important;
        }
        
        h2 {
            font-family: 'Inter', sans-serif !important;
            font-weight: 700 !important;
            color: #064E3B !important;
            font-size: 1.5rem !important;
            letter-spacing: -0.01em;
        }
        
        h3 {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            color: #065F46 !important;
            font-size: 1.25rem !important;
        }
        
        /* 6. SIDEBAR STYLING */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #ECFDF5 0%, #D1FAE5 100%);
            border-right: 1px solid rgba(5, 150, 105, 0.1);
        }
        
        [data-testid="stSidebar"] .block-container {
            padding-top: 2rem;
        }

        /* 7. PREMIUM INFO BOX */
        .info-box {
            background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
            padding: 24px 28px;
            border-radius: 16px;
            border-left: 4px solid;
            border-image: var(--accent-gradient) 1;
            margin-bottom: 24px;
            box-shadow: var(--shadow-md);
            position: relative;
            overflow: hidden;
        }

        .info-box::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 100px;
            height: 100px;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.15) 0%, transparent 70%);
            border-radius: 50%;
            transform: translate(30%, -30%);
        }
        
        .info-box p, .info-box li, .info-box span, .info-box h1, .info-box h2, .info-box h3 {
            color: #064E3B !important;
            -webkit-text-fill-color: #064E3B !important;
        }

        /* 8. PREMIUM BUTTONS */
        div.stButton > button {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600;
            background: var(--accent-gradient);
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            font-size: 0.95rem;
            letter-spacing: -0.01em;
            box-shadow: var(--shadow-green);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        div.stButton > button:hover {
            background: var(--accent-gradient-hover);
            transform: translateY(-3px);
            box-shadow: 0 15px 35px -10px rgba(5, 150, 105, 0.5);
        }

        div.stButton > button:active {
            transform: translateY(-1px);
        }

        /* Button ripple effect */
        div.stButton > button::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: width 0.3s, height 0.3s;
        }

        div.stButton > button:active::after {
            width: 200px;
            height: 200px;
        }

        /* 9. GLASSMORPHISM FEATURE CARDS */
        .feature-card {
            background: var(--glass-bg);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 32px 28px;
            border-radius: 20px;
            border: 1px solid rgba(16, 185, 129, 0.15);
            box-shadow: var(--shadow-lg);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: center;
            height: 100%;
            margin-bottom: 16px;
            position: relative;
            overflow: hidden;
        }

        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--accent-gradient);
            border-radius: 20px 20px 0 0;
        }
        
        .feature-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 25px 50px -12px rgba(5, 150, 105, 0.25);
            border-color: rgba(16, 185, 129, 0.3);
        }

        .feature-icon {
            font-size: 3rem;
            margin-bottom: 20px;
            display: block;
            filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1));
        }

        .feature-title {
            font-family: 'Inter', sans-serif !important;
            color: #047857 !important;
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 12px;
            display: block;
            letter-spacing: -0.01em;
        }

        .feature-desc {
            color: #4B5563 !important;
            font-size: 0.95rem;
            line-height: 1.6;
            font-weight: 400;
        }

        /* 10. PREMIUM METRIC CARDS */
        .metric-card {
            background: white;
            padding: 24px;
            border-radius: 16px;
            box-shadow: var(--shadow-md);
            border: 1px solid rgba(0, 0, 0, 0.05);
            text-align: center;
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            box-shadow: var(--shadow-xl);
            transform: translateY(-2px);
        }

        .metric-value {
            font-family: 'Inter', sans-serif !important;
            font-size: 2.5rem;
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.02em;
        }

        .metric-label {
            color: #6B7280;
            font-size: 0.9rem;
            font-weight: 500;
            margin-top: 8px;
        }

        /* 11. INPUT FIELDS */
        div[data-baseweb="input"] {
            border-radius: 12px !important;
            border: 2px solid #E5E7EB !important;
            transition: all 0.2s ease;
        }

        div[data-baseweb="input"]:focus-within {
            border-color: #10B981 !important;
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.15) !important;
        }
        
        div[data-baseweb="select"] {
            border-radius: 12px !important;
            border: 2px solid #E5E7EB !important;
        }

        /* 12. DATAFRAME STYLING */
        div[data-testid="stDataFrame"] {
            border: 1px solid rgba(16, 185, 129, 0.2);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: var(--shadow-md);
        }
        
        /* 13. FILE UPLOADER PREMIUM */
        [data-testid="stFileUploader"] {
            border: 2px dashed rgba(16, 185, 129, 0.4) !important;
            border-radius: 16px !important;
            background: linear-gradient(135deg, rgba(236, 253, 245, 0.5) 0%, rgba(209, 250, 229, 0.5) 100%);
            transition: all 0.3s ease;
        }

        [data-testid="stFileUploader"]:hover {
            border-color: #10B981 !important;
            background: linear-gradient(135deg, rgba(236, 253, 245, 0.8) 0%, rgba(209, 250, 229, 0.8) 100%);
        }

        /* 14. SUCCESS/WARNING/ERROR BOXES */
        div[data-testid="stAlert"] {
            border-radius: 12px !important;
            border: none !important;
            box-shadow: var(--shadow-sm);
        }

        /* 15. EXPANDER STYLING */
        details {
            border: 1px solid rgba(16, 185, 129, 0.2) !important;
            border-radius: 12px !important;
            background: white;
            overflow: hidden;
        }

        details summary {
            font-weight: 600;
            color: #047857;
        }

        /* 16. PROGRESS BAR */
        .stProgress > div > div {
            background: var(--accent-gradient);
            border-radius: 10px;
        }

        /* 17. SPINNER STYLING */
        .stSpinner > div {
            border-top-color: #10B981 !important;
        }

        /* 18. HORIZONTAL RULE */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(16, 185, 129, 0.3), transparent);
            margin: 2rem 0;
        }

        /* 19. TEAM CARD - PREMIUM */
        .team-card {
            background: white;
            border-radius: 20px;
            padding: 32px 24px;
            text-align: center;
            box-shadow: var(--shadow-lg);
            border: 1px solid rgba(0, 0, 0, 0.05);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .team-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 80px;
            background: var(--accent-gradient);
        }

        .team-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
        }

        .team-avatar {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 4px solid white;
            box-shadow: var(--shadow-lg);
            position: relative;
            z-index: 1;
            margin-top: 20px;
        }

        .team-name {
            font-family: 'Inter', sans-serif !important;
            font-size: 1.1rem;
            font-weight: 700;
            color: #1F2937;
            margin-top: 20px;
        }

        .team-nim {
            color: #6B7280;
            font-size: 0.9rem;
            margin: 8px 0;
        }

        .team-role {
            display: inline-block;
            background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
            color: #047857;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-top: 8px;
        }

        /* 20. CTA SECTION */
        .cta-section {
            background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
            padding: 40px;
            border-radius: 24px;
            text-align: center;
            border: 2px dashed rgba(16, 185, 129, 0.3);
            position: relative;
            overflow: hidden;
        }

        .cta-section::before,
        .cta-section::after {
            content: '';
            position: absolute;
            width: 150px;
            height: 150px;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.2) 0%, transparent 70%);
            border-radius: 50%;
        }

        .cta-section::before {
            top: -50px;
            left: -50px;
        }

        .cta-section::after {
            bottom: -50px;
            right: -50px;
        }

        /* 21. RESULT CARDS */
        .result-success {
            background: linear-gradient(135deg, #D1FAE5 0%, #A7F3D0 100%);
            padding: 24px;
            border-radius: 16px;
            border-left: 5px solid #10B981;
            color: #065F46 !important;
        }

        .result-danger {
            background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%);
            padding: 24px;
            border-radius: 16px;
            border-left: 5px solid #EF4444;
            color: #7F1D1D !important;
        }

        /* 22. SIDEBAR BRAND */
        .sidebar-brand {
            text-align: center;
            padding: 20px;
            margin-bottom: 20px;
        }

        .sidebar-brand h1 {
            font-size: 1.5rem !important;
            margin: 0 !important;
        }

        .sidebar-brand p {
            color: #6B7280;
            font-size: 0.85rem;
            margin: 8px 0 0 0;
        }

        /* 23. RADIO BUTTONS (Navigation) */
        [data-testid="stRadio"] > div {
            gap: 4px;
        }

        [data-testid="stRadio"] label {
            padding: 12px 16px !important;
            border-radius: 10px !important;
            transition: all 0.2s ease;
            font-weight: 500;
        }

        [data-testid="stRadio"] label:hover {
            background: rgba(16, 185, 129, 0.1);
        }

        /* 24. PAGE SUBTITLE */
        .page-subtitle {
            text-align: center;
            font-size: 1.15rem;
            color: #6B7280;
            margin-bottom: 40px;
            font-weight: 400;
            line-height: 1.6;
        }

        /* 25. HERO SECTION */
        .hero-section {
            text-align: center;
            padding: 20px 0 40px 0;
        }

        .hero-title {
            font-size: 2.75rem !important;
            font-weight: 800 !important;
            margin-bottom: 16px !important;
        }

        /* 26. ANIMATIONS */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.7;
            }
        }

        .animate-fade-in {
            animation: fadeInUp 0.5s ease-out;
        }

        /* 27. STATS GRID */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin: 24px 0;
        }

        .stat-item {
            background: white;
            padding: 20px;
            border-radius: 16px;
            text-align: center;
            box-shadow: var(--shadow-md);
            border: 1px solid rgba(0, 0, 0, 0.05);
        }

        .stat-number {
            font-size: 2rem;
            font-weight: 800;
            color: #047857;
        }

        .stat-label {
            font-size: 0.9rem;
            color: #6B7280;
            margin-top: 4px;
        }
        </style>
    """, unsafe_allow_html=True)