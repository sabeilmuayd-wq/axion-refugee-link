import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- إعدادات الهوية البصرية ---
st.set_page_config(page_title="Axion Refugee Link v2.0", page_icon="🌍", layout="wide")

# --- نظام الحماية (الدخول برقم الملف) ---
if "refugee_auth" not in st.session_state:
    st.markdown("<h1 style='text-align: center; color: #0089D1;'>🌍 Axion Refugee Link</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>نظام الكرامة الرقمية والتحول النوعي للاجئين</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        ref_id = st.text_input("أدخل رقم ملف اللجوء (UNHCR ID)", placeholder="UG-24-XXXXX")
        if st.button("دخول للنظام"):
            if ref_id:
                st.session_state["refugee_auth"] = ref_id
                st.rerun()
    st.stop()

# --- واجهة النظام الرئيسية ---
st.sidebar.image("https://img.icons8.com/fluency/96/user-male-circle.png")
st.sidebar.title(f"مرحباً، {st.session_state['refugee_auth']}")
st.sidebar.info("الحالة: لاجئ نشط - مؤهل لإعادة التوطين")

# --- القائمة العلوية ---
st.title("🛡️ منصة إدارة حقوق اللاجئين والمهارات")
st.write(f"التاريخ: {datetime.now().strftime('%Y-%m-%d')} | الموقع الحالي: كمبالا، أوغندا")

tab1, tab2, tab3, tab4 = st.tabs([
    "📅 جدولة الصرف الذكية", 
    "🍱 إدارة الحصص الغذائية", 
    "📊 سجل الكفاءات (الهجرة)", 
    "🛡️ الحماية والاستغاثة"
])

# --- القسم الأول: الجدولة (لإنهاء الزحام) ---
with tab1:
    st.header("📅 موعدك المخصص للصرف")
    st.info("نظام الجدولة يوزع المواعيد لمنع التكدس وحماية كبار السن والأطفال.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="تاريخ الاستلام القادم", value="18 مارس 2026")
        st.metric(label="الساعة المحددة", value="09:15 AM")
    with col_b:
        st.markdown("""
        **📍 مركز التوزيع:** Nsambya Settlement Hub  
        **📝 المطلوب:** إحضار الهاتف لعمل Scan للكود.  
        **✅ حالة الحضور:** تم تأكيد الموعد آلياً.
        """)
    
    # كود QR تخيلي للإبهار
    st.markdown("<div style='background-color:#eee; padding:20px; text-align:center; border: 2px dashed #333;'>QR CODE: [AX-SECURE-TOKEN-2026]</div>", unsafe_allow_html=True)

# --- القسم الثاني: الحصص للأسر (بما يتوافق مع أسرتك) ---
with tab2:
    st.header("🍱 مستحقات الأسرة (6 أفراد)")
    items = {
        "المادة الغذائية": ["ذرة (Maize Flour)", "زيت طعام", "بقوليات (Beans)", "كاش (Cash Aid)"],
        "الكمية المقررة": ["12kg x 6 = 72kg", "3L x 6 = 18L", "6kg x 6 = 36kg", "120,000 UGX"],
        "الحالة": ["✅ مستلم", "⏳ جاهز للصرف", "⏳ جاهز للصرف", "✅ تم التحويل"]
    }
    st.table(pd.DataFrame(items))

# --- القسم الثالث: سجل الكفاءات (هذا هو مفتاح الهجرة) ---
with tab3:
    st.header("🎓 سجل الكفاءات والخبرات")
    st.write("هذا القسم مصمم لموظفي إعادة التوطين لرؤية إمكانياتك الحقيقية.")
    
    c1, c2 = st.columns(2)
    with c1:
        skills = st.multiselect("المهارات التقنية والمهنية:", 
                                ["Software Engineering", "Agriculture", "Teaching", "Translation"],
                                default=["Software Engineering", "Agriculture"])
        experience = st.slider("سنوات الخبرة", 1, 20, 5)
    with c2:
        language = st.multiselect("اللغات:", ["Arabic", "English", "Luganda"], default=["Arabic", "English"])
        st.text_area("ملاحظات إضافية للمنظمة", "أعمل على تطوير أنظمة رقمية لتحسين كفاءة العمل الإنساني في الميدان.")

    if st.button("حفظ وتحديث ملف الهجرة"):
        st.success("تم تحديث ملفك بنجاح. سيتم إخطار قسم (Resettlement) بمهاراتك المحدثة.")

# --- القسم الرابع: الحماية ---
with tab4:
    st.header("🛡️ نظام الحماية والبلاغات")
    issue = st.selectbox("نوع البلاغ", ["مشكلة في الصرف", "فقدان وثائق", "حالة طبية طارئة", "أخرى"])
    detail = st.text_area("تفاصيل البلاغ")
    if st.button("إرسال بلاغ عاجل"):
        st.error("تم إرسال بلاغك لمكتب الحماية. رقم التتبع: PRO-9921")

st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>Axion Refugee Link | Developed by a Sudanese Innovator in Uganda</p>", unsafe_allow_html=True)
