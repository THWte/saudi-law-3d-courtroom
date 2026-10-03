import anthropic

client = anthropic.Anthropic()

class LegalAIBackend:
    """
    نظام قضائي ذكي متقدم - الخادم الخلفي
    Three Intelligence Modes + Continuous Learning
    """
    
    def __init__(self):
        self.saudi_laws = self.load_saudi_legal_system()
        self.case_memory = []
        self.learning_model = self.initialize_ml_model()
        self.response_cache = {}
        
    def load_saudi_legal_system(self):
        """تحميل قاعدة البيانات القانونية السعودية"""
        return {
            "basic_law": "نظام الحكم الأساسي للمملكة العربية السعودية",
            "civil_law": "نظام المرافعات الشرعية",
            "criminal_law": "نظام الإجراءات الجزائية",
            "commercial_law": "نظام الشركات والتجارة",
            "labor_law": "نظام العمل السعودي",
            "administrative_law": "القانون الإداري",
            "types": [
                "قضايا مدنية",
                "قضايا جزائية", 
                "قضايا تجارية",
                "قضايا عمل",
                "قضايا إدارية",
                "قضايا أحوال شخصية"
            ]
        }
    
    def initialize_ml_model(self):
        """تهيئة نموذج التعلم الآلي"""
        return {
            "precedent_analyzer": self.analyze_precedents,
            "risk_assessor": self.assess_risks,
            "strategy_planner": self.plan_strategy,
            "outcome_predictor": self.predict_outcome
        }
    
    # ====== الأنماط الثلاثة للذكاء ======
    
    def MODE_1_FULL_AI(self, case_data):
        """
        🤖 الوضع 1: ذكاء خالص - النظام يقرر بالكامل
        بدون تدخل المستخدم
        """
        analysis = self.deep_case_analysis(case_data)
        strategy = self.generate_strategy(analysis, "full_ai")
        recommendations = self.generate_recommendations(strategy)
        documents = self.generate_legal_documents(analysis, strategy)
        
        return {
            "mode": "FULL_AI",
            "analysis": analysis,
            "strategy": strategy,
            "recommendations": recommendations,
            "documents": documents,
            "confidence": analysis["confidence_score"],
            "action_plan": self.create_action_plan(strategy),
            "next_steps": self.auto_next_steps(strategy)
        }
    
    def MODE_2_AI_ASSISTED(self, case_data, user_input=None):
        """
        🤝 الوضع 2: مساعدة ذكية - تفاعل بين النظام والمستخدم
        النظام يقترح والمستخدم يختار
        """
        analysis = self.deep_case_analysis(case_data)
        
        # توليد خيارات متعددة
        options = {
            "strategies": self.generate_multiple_strategies(analysis, 3),
            "risk_levels": self.categorize_risks(analysis),
            "legal_grounds": self.find_legal_grounds(analysis),
            "precedents": self.find_similar_precedents(analysis, limit=5)
        }
        
        # إذا اختار المستخدم خياراً معيناً
        if user_input:
            selected_strategy = options["strategies"][user_input["strategy_choice"]]
            refined_analysis = self.refine_analysis(analysis, user_input)
            recommendations = self.generate_recommendations(refined_analysis)
        else:
            # توصيات افتراضية
            best_strategy = max(options["strategies"], key=lambda x: x["success_probability"])
            recommendations = self.generate_recommendations(best_strategy)
        
        return {
            "mode": "AI_ASSISTED",
            "options": options,
            "recommended": best_strategy if not user_input else selected_strategy,
            "user_can_adjust": True,
            "real_time_feedback": self.get_real_time_feedback(recommendations)
        }
    
    def MODE_3_USER_ONLY(self, case_data):
        """
        👤 الوضع 3: المستخدم فقط
        النظام يعرض المعلومات بدون اتخاذ قرارات
        """
        information = {
            "applicable_laws": self.get_applicable_laws(case_data),
            "relevant_articles": self.extract_relevant_articles(case_data),
            "similar_cases": self.find_similar_cases(case_data),
            "legal_procedures": self.get_procedures(case_data),
            "court_jurisdiction": self.determine_jurisdiction(case_data),
            "required_documents": self.get_required_documents(case_data),
            "legal_costs": self.estimate_legal_costs(case_data),
            "timeline": self.estimate_timeline(case_data)
        }
        
        return {
            "mode": "USER_ONLY",
            "information": information,
            "user_decides": True,
            "system_role": "Information provider only"
        }
    
    # ====== معالجة المدخلات الذكية ======
    
    def process_input(self, input_data):
        """معالجة جميع أنواع المدخلات بذكاء"""
        processed = {}
        
        # معالجة النص
        if input_data.get("text"):
            processed["text"] = self.nlp_analyze(input_data["text"])
        
        # معالجة الصوت
        if input_data.get("audio"):
            processed["voice"] = self.transcribe_audio(input_data["audio"])
        
        # معالجة الفيديو
        if input_data.get("video"):
            processed["video"] = self.extract_video_info(input_data["video"])
        
        # معالجة الصور
        if input_data.get("images"):
            processed["images"] = self.analyze_images(input_data["images"])
        
        # معالجة الملفات المرفقة
        if input_data.get("files"):
            processed["files"] = self.process_documents(input_data["files"])
        
        # معالجة الخيارات (checkboxes)
        if input_data.get("checkboxes"):
            processed["selections"] = self.process_selections(input_data["checkboxes"])
        
        # معالجة القوائم المنسدلة
        if input_data.get("dropdowns"):
            processed["dropdowns"] = input_data["dropdowns"]
        
        # معالجة النماذج الذكية
        if input_data.get("form_data"):
            processed["form"] = self.validate_form(input_data["form_data"])
        
        return processed
    
    def nlp_analyze(self, text):
        """تحليل النص بالمعالجة الطبيعية للغة"""
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": f"""أنت محلل قانوني سعودي ذكي. 
                    حلل النص التالي من قضية قانونية:
                    
                    {text}
                    
                    استخرج:
                    1. نوع القضية
                    2. الأطراف المعنية
                    3. الحقائق الأساسية
                    4. المطالبات
                    5. المستندات المرفقة المتوقعة
                    6. الأسس القانونية المحتملة
                    
                    رد بصيغة JSON منظمة."""
                }
            ]
        )
        
        return self.parse_response(message.content[0].text)
    
    def transcribe_audio(self, audio_file):
        """تحويل الصوت إلى نص"""
        # يتم استخدام مكتبة speech-to-text
        return {
            "transcript": "نص مستخرج من الصوت",
            "confidence": 0.95,
            "speaker_info": "معلومات المتحدث"
        }
    
    def extract_video_info(self, video_file):
        """استخراج المعلومات من الفيديو"""
        return {
            "transcript": "نص من الفيديو",
            "scenes": ["المشاهد المكتشفة"],
            "speakers": ["المتحدثون"],
            "duration": "المدة",
            "key_moments": ["اللحظات المهمة"]
        }
    
    def analyze_images(self, images):
        """تحليل الصور (مستندات، رسوم توضيحية)"""
        results = []
        for image in images:
            # OCR للنصوص في الصور
            text = self.ocr_extract(image)
            # كشف الأجسام والعناصر
            objects = self.detect_objects(image)
            
            results.append({
                "extracted_text": text,
                "detected_objects": objects,
                "quality_score": 0.9
            })
        
        return results
    
    def process_documents(self, files):
        """معالجة المستندات المرفقة (PDF, DOCX, etc)"""
        processed = []
        
        for file in files:
            if file.get("type") == "pdf":
                content = self.extract_pdf(file)
            elif file.get("type") == "docx":
                content = self.extract_docx(file)
            elif file.get("type") == "xlsx":
                content = self.extract_xlsx(file)
            else:
                content = self.extract_generic(file)
            
            processed.append({
                "filename": file.get("name"),
                "type": file.get("type"),
                "content": content,
                "extracted_entities": self.extract_entities(content)
            })
        
        return processed
    
    # ====== تحليل القضايا المتقدم ======
    
    def deep_case_analysis(self, case_data):
        """تحليل عميق للقضية"""
        processed_input = self.process_input(case_data)
        
        analysis = {
            "case_type": self.classify_case(processed_input),
            "parties": self.identify_parties(processed_input),
            "facts": self.extract_facts(processed_input),
            "claims": self.identify_claims(processed_input),
            "applicable_laws": self.find_applicable_laws(processed_input),
            "relevant_precedents": self.find_precedents(processed_input),
            "jurisdiction": self.determine_jurisdiction(processed_input),
            "risks": self.assess_risks(processed_input),
            "opportunities": self.identify_opportunities(processed_input),
            "confidence_score": self.calculate_confidence(processed_input)
        }
        
        return analysis
    
    def classify_case(self, data):
        """تصنيف نوع القضية"""
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[
                {
                    "role": "user",
                    "content": f"""صنف القضية التالية من بين:
                    - قضايا مدنية
                    - قضايا جزائية
                    - قضايا تجارية
                    - قضايا عمل
                    - قضايا إدارية
                    - قضايا أحوال شخصية
                    
                    البيانات: {str(data)[:1000]}
                    
                    رد بالتصنيف الأدق فقط."""
                }
            ]
        )
        
        return message.content[0].text.strip()
    
    def identify_parties(self, data):
        """تحديد الأطراف المعنية"""
        return {
            "plaintiff": self.extract_plaintiff(data),
            "defendant": self.extract_defendant(data),
            "third_parties": self.extract_third_parties(data),
            "representatives": self.extract_representatives(data)
        }
    
    def assess_risks(self, analysis):
        """تقييم المخاطر القانونية"""
        risks = []
        
        for aspect in ["legal", "procedural", "financial", "reputational"]:
            risk_level = self.calculate_risk_level(analysis, aspect)
            risks.append({
                "aspect": aspect,
                "level": risk_level,
                "description": self.describe_risk(analysis, aspect),
                "mitigation": self.suggest_mitigation(aspect)
            })
        
        return risks
    
    def predict_outcome(self, analysis):
        """التنبؤ بنتيجة القضية"""
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": f"""بناءً على التحليل القانوني التالي، تنبأ بنتيجة القضية:
                    
                    نوع القضية: {analysis['case_type']}
                    الحقائق: {analysis['facts']}
                    القوانين المنطبقة: {analysis['applicable_laws']}
                    الأحكام السابقة ذات الصلة: {analysis['relevant_precedents']}
                    
                    قدم:
                    1. احتمالية الفوز/الخسارة (نسبة مئوية)
                    2. السيناريوهات المحتملة
                    3. التوصيات للحصول على أفضل نتيجة"""
                }
            ]
        )
        
        return self.parse_response(message.content[0].text)
    
    # ====== التعلم المستمر والنمو التراكمي ======
    
    def learn_from_case(self, case_id, outcome):
        """التعلم من كل قضية مغلقة"""
        self.case_memory.append({
            "case_id": case_id,
            "outcome": outcome,
            "learned_patterns": self.extract_patterns(outcome),
            "timestamp": self.get_timestamp()
        })
        
        # تحديث النموذج
        self.update_prediction_model()
        
        # حفظ في الذاكرة طويلة الأجل
        self.save_to_persistent_memory(case_id, outcome)
    
    def update_prediction_model(self):
        """تحديث نموذج التنبؤ بناءً على الحالات الجديدة"""
        if len(self.case_memory) > 10:
            patterns = self.aggregate_patterns()
            self.learning_model["predictor"] = self.retrain_model(patterns)
    
    # ====== توليد المخرجات الذكية ======
    
    def generate_strategy(self, analysis, mode):
        """توليد استراتيجية قانونية شاملة"""
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=3000,
            messages=[
                {
                    "role": "user",
                    "content": f"""أنت محامي سعودي خبير. طور استراتيجية قانونية شاملة للقضية التالية:
                    
                    {str(analysis)[:2000]}
                    
                    الوضع: {mode}
                    
                    قدم:
                    1. الاستراتيجية الرئيسية
                    2. الخطوات الإجرائية بالترتيب
                    3. البدائل والخيارات
                    4. الأدلة المطلوب تجميعها
                    5. الشهود المطلوبون
                    6. المستندات القانونية المطلوبة
                    7. المحاذير والتحديات المتوقعة
                    8. مؤشرات النجاح"""
                }
            ]
        )
        
        return self.parse_response(message.content[0].text)
    
    def generate_legal_documents(self, analysis, strategy):
        """توليد المستندات القانونية تلقائياً"""
        return {
            "complaint": self.generate_complaint(analysis),
            "evidence_list": self.generate_evidence_list(analysis),
            "witness_list": self.generate_witness_list(analysis),
            "legal_brief": self.generate_legal_brief(strategy),
            "motions": self.generate_motions(analysis),
            "agreements": self.generate_agreements(analysis)
        }
    
    def generate_recommendations(self, strategy):
        """توليد التوصيات المخصصة"""
        return {
            "immediate_actions": strategy.get("immediate_actions", []),
            "short_term": strategy.get("short_term_plans", []),
            "long_term": strategy.get("long_term_plans", []),
            "risk_mitigation": strategy.get("risk_mitigation", []),
            "success_factors": strategy.get("success_factors", [])
        }
    
    # ====== دعم الأداء والسرعة ======
    
    def parse_response(self, response):
        """معالجة وتنظيم الردود"""
        try:
            import json
            return json.loads(response)
        except:
            return {"raw": response}
    
    def get_timestamp(self):
        """الحصول على الوقت والتاريخ الحالي"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def cache_response(self, key, value):
        """تخزين مؤقت للاستجابات المتكررة"""
        self.response_cache[key] = value
    
    def get_cached_response(self, key):
        """استرجاع من الذاكرة المؤقتة"""
        return self.response_cache.get(key)


# ====== دالة رئيسية للاستخدام ======

def process_legal_case(case_data, mode="AI_ASSISTED"):
    """
    معالجة قضية قانونية بناءً على الوضع المختار
    
    Args:
        case_data: بيانات القضية
        mode: FULL_AI | AI_ASSISTED | USER_ONLY
    
    Returns:
        تحليل شامل وتوصيات
    """
    ai_system = LegalAIBackend()
    
    if mode == "FULL_AI":
        return ai_system.MODE_1_FULL_AI(case_data)
    elif mode == "AI_ASSISTED":
        return ai_system.MODE_2_AI_ASSISTED(case_data)
    elif mode == "USER_ONLY":
        return ai_system.MODE_3_USER_ONLY(case_data)
    else:
        return {"error": "وضع غير معروف"}


if __name__ == "__main__":
    # مثال على الاستخدام
    test_case = {
        "text": "قضية نزاع تجاري حول عقد شراء بضائع",
        "checkboxes": ["مدعي", "مدعى عليه"],
        "dropdowns": ["قضائي", "تجاري"]
    }
    
    result = process_legal_case(test_case, mode="AI_ASSISTED")
    print(result)
