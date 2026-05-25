import streamlit as st

st.title("🧮 Calculateur de leçons - By Florence")

# =========================
# ANNÉE
# =========================
annee = st.number_input("📅 Année", min_value=2000, max_value=3000, value=2026)


# =========================
# DURÉE DES ACTIVITÉS
# =========================

with st.expander("⏱️ Durée des activités (en minutes)", expanded=False):

    st.write("Entrez la durée de leçon")

    durees = [30, 45, 60, 75, 90, 105, 120]


    duree_p = st.selectbox("Muscu", durees, index=2, key="duree_p")
    duree_o = st.selectbox("Grande salle", durees, index=2, key="duree_o")
    duree_m = st.selectbox("Petite salle", durees, index=2, key="duree_m")

    duree_x = st.selectbox("Forum", durees, index=2, key="duree_x")
    duree_y = st.selectbox("Comète", durees, index=2, key="duree_y")
    duree_z = st.selectbox("CES", durees, index=2, key="duree_z")
    duree_a = st.selectbox("Rue du Ballon", durees, index=2, key="duree_a")
    duree_b = st.selectbox("Stade", durees, index=2, key="duree_b")
    duree_c = st.selectbox("Piscine", durees, index=2, key="duree_c")
    duree_d = st.selectbox("SAE", durees, index=2, key="duree_d")
    duree_e = st.selectbox("Multi Cosec", durees, index=2, key="duree_e")



# =========================
# SEMESTRE 1
# =========================
with st.expander(f"📘 Semestre 1 ({annee})", expanded=False):

    st.write("Entrez le nombre de leçons pour chaque catégorie")

    st.subheader("Intra")
    s1_p = st.number_input("Muscu", min_value=0, value=0, key="s1_p")
    s1_o = st.number_input("Grande salle", min_value=0, value=0, key="s1_o")
    s1_m = st.number_input("Petite salle", min_value=0, value=0, key="s1_m")

    st.subheader("Extra")
    s1_x = st.number_input("Forum", min_value=0, value=0, key="s1_x")
    s1_y = st.number_input("Comète", min_value=0, value=0, key="s1_y")
    s1_z = st.number_input("CES", min_value=0, value=0, key="s1_z")
    s1_a = st.number_input("Rue du Ballon", min_value=0, value=0, key="s1_a")
    s1_b = st.number_input("Stade", min_value=0, value=0, key="s1_b")
    s1_c = st.number_input("Piscine", min_value=0, value=0, key="s1_c")
    s1_d = st.number_input("SAE", min_value=0, value=0, key="s1_d")
    s1_e = st.number_input("Multi Cosec", min_value=0, value=0, key="s1_e")

    st.subheader("🎓 Stage")
    s1_stage = st.number_input("Nombre de leçons stage (semestre 1)", min_value=0, value=0, key="s1_stage")


# =========================
# SEMESTRE 2
# =========================
with st.expander(f"📙 Semestre 2 ({annee})", expanded=False):

    st.write("Entrez le nombre de leçons pour chaque catégorie")

    st.subheader("Intra")
    s2_p = st.number_input("Muscu", min_value=0, value=0, key="s2_p")
    s2_o = st.number_input("Grande salle", min_value=0, value=0, key="s2_o")
    s2_m = st.number_input("Petite salle", min_value=0, value=0, key="s2_m")

    st.subheader("Extra")
    s2_x = st.number_input("Forum", min_value=0, value=0, key="s2_x")
    s2_y = st.number_input("Comète", min_value=0, value=0, key="s2_y")
    s2_z = st.number_input("CES", min_value=0, value=0, key="s2_z")
    s2_a = st.number_input("Rue du Ballon", min_value=0, value=0, key="s2_a")
    s2_b = st.number_input("Stade", min_value=0, value=0, key="s2_b")
    s2_c = st.number_input("Piscine", min_value=0, value=0, key="s2_c")
    s2_d = st.number_input("SAE", min_value=0, value=0, key="s2_d")
    s2_e = st.number_input("Multi Cosec", min_value=0, value=0, key="s2_e")

    st.subheader("🎓 Stage")
    s2_stage = st.number_input("Nombre de leçons stage (semestre 2)", min_value=0, value=0, key="s2_stage")


# =========================
# CALCULS
# =========================

s1_intra = s1_p + s1_o + s1_m
s1_extra = s1_x + s1_y + s1_z + s1_a + s1_b + s1_c + s1_d + s1_e
s1_total = s1_intra + s1_extra - s1_stage

s2_intra = s2_p + s2_o + s2_m
s2_extra = s2_x + s2_y + s2_z + s2_a + s2_b + s2_c + s2_d + s2_e
s2_total = s2_intra + s2_extra - s2_stage

annee_total = s1_total + s2_total


# Totaux par lettre (année)
tot_p = s1_p + s2_p
tot_o = s1_o + s2_o
tot_m = s1_m + s2_m

tot_x = s1_x + s2_x
tot_y = s1_y + s2_y
tot_z = s1_z + s2_z
tot_a = s1_a + s2_a
tot_b = s1_b + s2_b
tot_c = s1_c + s2_c
tot_d = s1_d + s2_d
tot_e = s1_e + s2_e

# =========================
# CALCUL DES HEURES
# =========================



minutes_s1 = (
    s1_p * duree_p +
    s1_o * duree_o +
    s1_m * duree_m +
    s1_x * duree_x +
    s1_y * duree_y +
    s1_z * duree_z +
    s1_a * duree_a +
    s1_b * duree_b +
    s1_c * duree_c +
    s1_d * duree_d +
    s1_e * duree_e
)

minutes_s2 = (
    s2_p * duree_p +
    s2_o * duree_o +
    s2_m * duree_m +
    s2_x * duree_x +
    s2_y * duree_y +
    s2_z * duree_z +
    s2_a * duree_a +
    s2_b * duree_b +
    s2_c * duree_c +
    s2_d * duree_d +
    s2_e * duree_e
)

heures_s1 = round(minutes_s1 / 60, 2)
heures_muscu = round(duree_p * s1_p / 60, 2)
heures_grandesalle = round(duree_o * s1_o / 60, 2) 
heures_petitesalle = round(duree_m * s1_m / 60, 2)
heures_forum = round(duree_x * s1_x / 60, 2)
heures_comete = round(duree_y * s1_y / 60, 2)
heures_ces = round(duree_z * s1_z / 60, 2)
heures_rueballon = round(duree_a * s1_a/ 60, 2)
heures_stade = round(duree_b * s1_b/ 60, 2)
heures_piscine = round(duree_c * s1_c/ 60, 2)
heures_sae = round(duree_d * s1_d/ 60, 2)
heures_multicosec = round(duree_e * s1_e/ 60, 2)
heures_intra = round(heures_muscu + heures_grandesalle + heures_petitesalle)
heures_extra = round(heures_forum + heures_comete + heures_ces + heures_rueballon + heures_piscine + heures_sae + heures_multicosec)
heures_stage = round(s1_stage * 2)
heures_s2 = round(minutes_s2 / 60, 2)
heures_muscu1 = round(duree_p * s2_p / 60, 2)
heures_grandesalle1 = round(duree_o * s2_o / 60, 2) 
heures_petitesalle1 = round(duree_m * s2_m / 60, 2)
heures_forum1 = round(duree_x * s2_x / 60, 2)
heures_comete1 = round(duree_y * s2_y / 60, 2)
heures_ces1 = round(duree_z * s2_z / 60, 2)
heures_rueballon1 = round(duree_a * s2_a/ 60, 2)
heures_stade1 = round(duree_b * s2_b/ 60, 2)
heures_piscine1 = round(duree_c * s2_c/ 60, 2)
heures_sae1 = round(duree_d * s2_d/ 60, 2)
heures_multicosec1 = round(duree_e * s2_e/ 60, 2)
heures_intra1 = round(heures_muscu1 + heures_grandesalle1 + heures_petitesalle1)
heures_extra1 = round(heures_forum1 + heures_comete1 + heures_ces1 + heures_rueballon1 + heures_piscine1 + heures_sae1 + heures_multicosec1)
heures_stage1 = round(s2_stage * 2)
heures_annee = round((minutes_s1 + minutes_s2) / 60, 2)



# =========================
# AFFICHAGE
# =========================
if st.button("📊 Calculer"):

    st.subheader(f"🗒️ Résultats année {annee}")

    with st.expander(f"📘 Semestre 1 ({annee})", expanded=False):
     with st.expander(f"Intra : {s1_intra} leçons ({heures_intra}h)", expanded=False):
        st.write(f"Muscu : {s1_p} leçons ({heures_muscu}h)")
        st.write(f"Grande salle : {s1_o} leçons ({heures_grandesalle}h)")
        st.write(f"Petite salle : {s1_m} leçons ({heures_petitesalle}h)")
     with st.expander(f"Extra : {s1_extra} leçons ({heures_extra}h)", expanded=False):
        st.write(f"Forum : {s1_x} leçons ({heures_forum}h)")
        st.write(f"Comète : {s1_y} leçons ({heures_comete}h)")
        st.write(f"CES : {s1_z} leçons ({heures_ces}h)")
        st.write(f"Rue du Ballon : {s1_a} leçons ({heures_rueballon}h)")
        st.write(f"Stade : {s1_b} leçons ({heures_stade}h)")
        st.write(f"Piscine : {s1_c} leçons ({heures_piscine}h")
        st.write(f"SAE : {s1_d} leçons ({s1_d}h)")
        st.write(f"Multi Cosec : {s1_e} leçons ({heures_multicosec}h)")
        st.write(f"Stage : -{s1_stage} leçons ({heures_stade}h)")

    with st.expander(f"📙 Semestre 2 ({annee})", expanded=False):
     with st.expander(f"Intra : {s2_intra} leçons ({heures_intra1}h)", expanded=False):
        st.write(f"Muscu : {s2_p} leçons ({heures_muscu1}h)")
        st.write(f"Grande salle : {s2_o} leçons ({heures_grandesalle1}h)")
        st.write(f"Petite salle : {s2_m} leçons ({heures_petitesalle1}h)")
     with st.expander(f"Extra : {s2_extra} leçons ({heures_extra1}h)", expanded=False):
        st.write(f"Forum : {s2_x} leçons ({heures_forum1}h)")
        st.write(f"Comète : {s2_y} leçons ({heures_comete1}h)")
        st.write(f"CES : {s2_z} leçons ({heures_ces1}h)")
        st.write(f"Rue du Ballon : {s2_a} leçons ({heures_rueballon1}h)")
        st.write(f"Stade : {s2_b} leçons ({heures_stade1}h)")
        st.write(f"Piscine : {s2_c} leçons ({heures_piscine1}h)")
        st.write(f"SAE : {s2_d} leçons ({heures_sae1}h)")
        st.write(f"Multi Cosec : {s2_e} leçons ({heures_multicosec1}h)")
        st.write(f"Stage : -{s2_stage} leçons ({heures_stage1}h)")

    st.subheader(f"📆 Bilan année {annee}")

    st.success(f"📘 Bilan semestre 1 de {annee} : {s1_total} leçons ({heures_s1} h)")
    st.success(f"📙 Bilan semestre 2 de {annee} : {s2_total} leçons ({heures_s2} h)")
    st.success(f"🎓 Bilan année (civile) {annee} : {annee_total} leçons ({heures_annee} h)")
