from django import forms
from pages.models import Post

valve_type_tuple = (
	('', 'Select an option...'),
	('BALL', 'BALL'),
	('BUTTERFLY', 'BUTTERFLY'),
)

body_size_tuple = (
	('', 'Select an option...'),
	('0.5', '0.5'),
	('0.75', '0.75'),
	('1', '1'),
	('1.5', '1.5'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('6', '6'),
	('8', '8'),
	('10', '10'),
	('12', '12'),
	('14', '14'),
	('16', '16'),
	('18', '18'),
	('20', '20'),
	('22', '22'),
	('24', '24'),
	('26', '26'),
	('28', '28'),
	('30', '30'),
	('32', '32'),
	('34', '34'),
	('36', '36'),
	('38', '38'),
	('40', '40'),
	('42', '42'),
	('44', '44'),
	('46', '46'),
	('48', '48'),
	('50', '50'),
	('52', '52'),
	('54', '54'),
	('56', '56'),
	('58', '58'),
	('60', '60'),
)

body_material_tuple = (
	('', 'Select an option...'),
	('17-4 PH H1150D', '17-4 PH H1150D'),
	('A105', 'A105'),
	('A182 F304', 'A182 F304'),
	('A182 F316', 'A182 F316'),
	('A182 F44', 'A182 F44'),
	('A182 F51', 'A182 F51'),
	('A182 F53', 'A182 F53'),
	('A182 F55', 'A182 F55'),
	('A182 F6a', 'A182 F6a'),
	('A182 F6NM', 'A182 F6NM'),
	('A182 F91', 'A182 F91'),
	('A182 XM19', 'A182 XM19'),
	('A216 CA15', 'A216 CA15'),
	('A216 WCB', 'A216 WCB'),
	('A216 WCC', 'A216 WCC'),
	('A350 LF2', 'A350 LF2'),
	('A351 CA6NM', 'A351 CA6NM'),
	('A351 CF3M', 'A351 CF3M'),
	('A351 CF8M', 'A351 CF8M'),
	('A351 CK3MCuN', 'A351 CK3MCuN'),
	('A351 CK3MCuN', 'A351 CK3MCuN'),
	('A352 LCB', 'A352 LCB'),
	('A352 LCC', 'A352 LCC'),
	('A494 Cu5MCuC', 'A494 Cu5MCuC'),
	('A494 Cu5MCuC', 'A494 Cu5MCuC'),
	('A494 CW6-MC', 'A494 CW6-MC'),
	('A494 CW6-MC', 'A494 CW6-MC'),
	('A694 F65 (API 6A-60K)', 'A694 F65 (API 6A-60K)'),
	('A995 Gr. 4A', 'A995 Gr. 4A'),
	('A995 Gr. 5A', 'A995 Gr. 5A'),
	('A995 Gr. 6A', 'A995 Gr. 6A'),
	('AISI 4130 (API6A-60K)', 'AISI 4130 (API6A-60K)'),
	('AISI 4130 (API6A-75K)', 'AISI 4130 (API6A-75K)'),
	('ALLOY 625', 'ALLOY 625'),
	('ALLOY 825', 'ALLOY 825'),
	('ALLOY 925', 'ALLOY 925'),
	('ALLOY 926', 'ALLOY 926'),
	('API 6A-718', 'API 6A-718'),
	('HASTELLOY', 'HASTELLOY'),
	('MONEL 400', 'MONEL 400'),
	('MONEL K400', 'MONEL K400'),
	('MONEL K500', 'MONEL K500'),
	('MONEL K500 FUSO', 'MONEL K500 FUSO'),
	('NA', 'NA'),
	('NITRONIC 50', 'NITRONIC 50'),
	('TITANIO Gr.2', 'TITANIO Gr.2'),
	('TITANIO Gr.5', 'TITANIO Gr.5'),
)

rating_tuple = (
	('', 'Select an option...'),
	('CL 150', 'CL 150'),
	('CL 300', 'CL 300'),
	('CL 400', 'CL 400'),
	('CL 600', 'CL 600'),
	('CL 800', 'CL 800'),
	('CL 900', 'CL 900'),
	('CL 1500', 'CL 1500'),
	('CL 2000', 'CL 2000'),
	('CL 2500', 'CL 2500'),
	('CL 3000', 'CL 3000'),
	('CL 4500', 'CL 4500'),
	('CL 5000', 'CL 5000'),
	('CL 10000', 'CL 10000'),
	('CL 15000', 'CL 15000'),
)

end_connections_tuple = (
	('', 'Select an option...'),
	('Butt Weld', 'Butt Weld'),
	('Socket Weld', 'Socket Weld'),
	('Flanged RF', 'Flanged RF'),
	('Flanged RTJ', 'Flanged RTJ'),
)
stem_material_tuple = (
	('', 'Select an option...'),
	('17-4 PH H1150D', '17-4 PH H1150D'),
	('A182 F44', 'A182 F44'),
	('A182 F51', 'A182 F51'),
	('A182 F53', 'A182 F53'),
	('A182 F55', 'A182 F55'),
	('A182 F6a', 'A182 F6a'),
	('A182 F6NM', 'A182 F6NM'),
	('A694 F65 (API 6A-60K)', 'A694 F65 (API 6A-60K)'),
	('AISI 4130 (API6A-60K)', 'AISI 4130 (API6A-60K)'),
	('AISI 4130 (API6A-75K)', 'AISI 4130 (API6A-75K)'),
	('ALLOY 625', 'ALLOY 625'),
	('ALLOY 925', 'ALLOY 925'),
	('ALLOY 926', 'ALLOY 926'),
	('API 6A-718', 'API 6A-718'),
	('NITRONIC 50', 'NITRONIC 50'),
	('TITANIO Gr.5', 'TITANIO Gr.5'),
	('A694 F65 ', 'A694 F65 '),
	('AISI 4130 ', 'AISI 4130 '),
)
seat_material_tuple = (
	('', 'Select an option...'),
	('17-4 PH H1150D', '17-4 PH H1150D'),
	('A105', 'A105'),
	('A182 F304', 'A182 F304'),
	('A182 F316', 'A182 F316'),
	('A182 F44', 'A182 F44'),
	('A182 F51', 'A182 F51'),
	('A182 F53', 'A182 F53'),
	('A182 F55', 'A182 F55'),
	('A182 F6a', 'A182 F6a'),
	('A182 F6NM', 'A182 F6NM'),
	('A182 XM19', 'A182 XM19'),
	('A216 CA15', 'A216 CA15'),
	('A350 LF2', 'A350 LF2'),
	('A351 CA6NM', 'A351 CA6NM'),
	('A351 CF3M', 'A351 CF3M'),
	('A351 CF8M', 'A351 CF8M'),
	('A351 CK3MCuN', 'A351 CK3MCuN'),
	('A494 Cu5MCuC', 'A494 Cu5MCuC'),
	('A494 CW6-MC', 'A494 CW6-MC'),
	('A694 F65 (API 6A-60K)', 'A694 F65 (API 6A-60K)'),
	('A995 Gr. 4A', 'A995 Gr. 4A'),
	('A995 Gr. 5A', 'A995 Gr. 5A'),
	('A995 Gr. 6A', 'A995 Gr. 6A'),
	('ALLOY 625', 'ALLOY 625'),
	('ALLOY 825', 'ALLOY 825'),
	('ALLOY 925', 'ALLOY 925'),
	('ALLOY 926', 'ALLOY 926'),
	('API 6A-718', 'API 6A-718'),
	('HASTELLOY', 'HASTELLOY'),
	('MONEL 400', 'MONEL 400'),
	('MONEL K400', 'MONEL K400'),
	('MONEL K500 FUSO', 'MONEL K500 FUSO'),
	('TITANIO Gr.2', 'TITANIO Gr.2'),
	('TITANIO Gr.5', 'TITANIO Gr.5'),
	('A216 CA15', 'A216 CA15'),
	('A351 CA6NM', 'A351 CA6NM'),
	('A351 CF8M', 'A351 CF8M'),
	('A351 CF3M', 'A351 CF3M'),
	('A995 Gr. 4A', 'A995 Gr. 4A'),
	('A995 Gr. 5A', 'A995 Gr. 5A'),
	('A995 Gr. 6A', 'A995 Gr. 6A'),
	('A351 CK3MCuN', 'A351 CK3MCuN'),
	('A494 Cu5MCuC', 'A494 Cu5MCuC'),
	('A494 CW6-MC', 'A494 CW6-MC'),
	('MONEL K500 FUSO', 'MONEL K500 FUSO'),
	('A351 CF8', 'A351 CF8'),
	('A694 F65 ', 'A694 F65 '),
)
bonnet_bolting_material_tuple = (
	('', 'Select an option...'),
	('BOLTING', 'BOLTING'),
	('ALLOY 625', 'ALLOY 625'),
	('B7/2H', 'B7/2H'),
	('B7M/2HM', 'B7M/2HM'),
	('L7/7', 'L7/7'),
	('L7M/7M', 'L7M/7M'),
	('B8 Cl.1 /8', 'B8 Cl.1 /8'),
	('B8 Cl.2 /8', 'B8 Cl.2 /8'),
	('B8M/8M', 'B8M/8M'),
	('Gr. 660', 'Gr. 660'),
	('Alloy 718', 'Alloy 718'),
	('Titanio', 'Titanio'),
)
trim_type_tuple = (
	('', 'Select an option...'),
	('BALL', 'BALL'),
	('SEGMENT BALL', 'SEGMENT BALL'),
	('CONCENTRIC DISC', 'CONCENTRIC DISC'),
	('ECCENTRIC DISC', 'ECCENTRIC DISC'),
)
trim_size_tuple = (
	('', 'Select an option...'),
	('0.5', '0.5'),
	('0.75x0.5', '0.75x0.5'),
	('0.75', '0.75'),
	('1x0.75', '1x0.75'),
	('1', '1'),
	('1.5x1', '1.5x1'),
	('1.5', '1.5'),
	('2x1.5', '2x1.5'),
	('2', '2'),
	('3x2', '3x2'),
	('3', '3'),
	('4x3', '4x3'),
	('4', '4'),
	('6x4', '6x4'),
	('6', '6'),
	('8x6', '8x6'),
	('8', '8'),
	('10x8', '10x8'),
	('10', '10'),
	('12x10', '12x10'),
	('14x10', '14x10'),
	('12', '12'),
	('14x12', '14x12'),
	('16x12', '16x12'),
	('14', '14'),
	('16x14', '16x14'),
	('18x14', '18x14'),
	('16', '16'),
	('18x16', '18x16'),
	('20x16', '20x16'),
	('18', '18'),
	('20x18', '20x18'),
	('22x18', '22x18'),
	('20', '20'),
	('24x20', '24x20'),
	('22', '22'),
	('24', '24'),
	('28x24', '28x24'),
	('30x24', '30x24'),
	('26', '26'),
	('32x26', '32x26'),
	('28', '28'),
	('34x28', '34x28'),
	('30', '30'),
	('36x30', '36x30'),
	('32', '32'),
	('38x32', '38x32'),
	('34', '34'),
	('40x34', '40x34'),
	('36', '36'),
	('40x36', '40x36'),
	('38', '38'),
	('40', '40'),
	('48x40', '48x40'),
	('42', '42'),
	('54x42', '54x42'),
	('56x42', '56x42'),
	('44', '44'),
	('46', '46'),
	('48', '48'),
	('60x48', '60x48'),
	('50', '50'),
	('52', '52'),
	('54', '54'),
	('56', '56'),
	('58', '58'),
	('60', '60'),
)
trim_material_tuple = (
	('', 'Select an option...'),
	('17-4 PH H1150D', '17-4 PH H1150D'),
	('A105', 'A105'),
	('A182 F304', 'A182 F304'),
	('A182 F316', 'A182 F316'),
	('A182 F44', 'A182 F44'),
	('A182 F51', 'A182 F51'),
	('A182 F53', 'A182 F53'),
	('A182 F55', 'A182 F55'),
	('A182 F6a', 'A182 F6a'),
	('A182 F6NM', 'A182 F6NM'),
	('A182 XM19', 'A182 XM19'),
	('A216 CA15', 'A216 CA15'),
	('A350 LF2', 'A350 LF2'),
	('A351 CA6NM', 'A351 CA6NM'),
	('A351 CF3M', 'A351 CF3M'),
	('A351 CF8M', 'A351 CF8M'),
	('A351 CK3MCuN', 'A351 CK3MCuN'),
	('A494 Cu5MCuC', 'A494 Cu5MCuC'),
	('A494 CW6-MC', 'A494 CW6-MC'),
	('A694 F65 (API 6A-60K)', 'A694 F65 (API 6A-60K)'),
	('A995 Gr. 4A', 'A995 Gr. 4A'),
	('A995 Gr. 5A', 'A995 Gr. 5A'),
	('A995 Gr. 6A', 'A995 Gr. 6A'),
	('ALLOY 625', 'ALLOY 625'),
	('ALLOY 825', 'ALLOY 825'),
	('ALLOY 925', 'ALLOY 925'),
	('ALLOY 926', 'ALLOY 926'),
	('API 6A-718', 'API 6A-718'),
	('HASTELLOY', 'HASTELLOY'),
	('MONEL 400', 'MONEL 400'),
	('MONEL K400', 'MONEL K400'),
	('MONEL K500 FUSO', 'MONEL K500 FUSO'),
	('TITANIO Gr.2', 'TITANIO Gr.2'),
	('TITANIO Gr.5', 'TITANIO Gr.5'),
	('A216 CA15', 'A216 CA15'),
	('A351 CA6NM', 'A351 CA6NM'),
	('A351 CF8M', 'A351 CF8M'),
	('A351 CF3M', 'A351 CF3M'),
	('A995 Gr. 4A', 'A995 Gr. 4A'),
	('A995 Gr. 5A', 'A995 Gr. 5A'),
	('A995 Gr. 6A', 'A995 Gr. 6A'),
	('A351 CK3MCuN', 'A351 CK3MCuN'),
	('A494 Cu5MCuC', 'A494 Cu5MCuC'),
	('A494 CW6-MC', 'A494 CW6-MC'),
	('MONEL K500 FUSO', 'MONEL K500 FUSO'),
	('A351 CF8', 'A351 CF8'),
	('A694 F65 ', 'A694 F65 '),
)
leakage_class_tuple = (
	('', 'Select an option...'),
	('IEC 60534 class I', 'IEC 60534 class I'),
	('IEC 60534 class II', 'IEC 60534 class II'),
	('IEC 60534 class III', 'IEC 60534 class III'),
	('IEC 60534 class IV', 'IEC 60534 class IV'),
	('IEC 60534 class V', 'IEC 60534 class V'),
	('IEC 60534 class VI', 'IEC 60534 class VI'),
	('API 598 soft seat', 'API 598 soft seat'),
	('API 598 metal seat', 'API 598 metal seat'),
	('ISO 5208 rate A', 'ISO 5208 rate A'),
	('ISO 5208 rate AA', 'ISO 5208 rate AA'),
	('ISO 5208 rate B', 'ISO 5208 rate B'),
	('ISO 5208 rate C', 'ISO 5208 rate C'),
	('ISO 5208 rate CC', 'ISO 5208 rate CC'),
	('ISO 5208 rate D', 'ISO 5208 rate D'),
	('ISO 5208 rate E', 'ISO 5208 rate E'),
	('ISO 5208 rate EE', 'ISO 5208 rate EE'),
	('ISO 5208 rate F', 'ISO 5208 rate F'),
	('ISO 5208 rate G', 'ISO 5208 rate G'),
)
fire_safe_tuple = (
	('', 'Select an option...'),
	('API 607 - 6FA', 'API 607 - 6FA'),
)
nace_requirement_tuple = (
	('', 'Select an option...'),
	('NACE MR 01-03', 'NACE MR 01-03'),
	('NACE MR 01-75', 'NACE MR 01-75'),
)


class TestForm(forms.ModelForm):
	m_valve_type = forms.ChoiceField(required=False, label= 'Valve Type:', choices=valve_type_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		#'id': 'inputState',
		#'rows': '3',
		}))
	m_body_size = forms.ChoiceField(required=False, label= 'Body Size:', choices=body_size_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_body_material = forms.ChoiceField(required=False, label= 'Body Material:', choices=body_material_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_rating = forms.ChoiceField(required=False, label= 'Rating:', choices=rating_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_end_connections = forms.ChoiceField(required=False, label= 'End Connections:', choices=end_connections_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_stem_material = forms.ChoiceField(required=False, label= 'Stem Material:', choices=stem_material_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_seat_material = forms.ChoiceField(required=False, label= 'Seat Material:', choices=seat_material_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_bonnet_bolting_material = forms.ChoiceField(required=False, label= 'Bonnet Bolting Material:', choices=bonnet_bolting_material_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_trim_type = forms.ChoiceField(required=False, label= 'Trim Type:', choices=trim_type_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_trim_size = forms.ChoiceField(required=False, label= 'Trim Size:', choices=trim_size_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_trim_material = forms.ChoiceField(required=False, label= 'Trim Material:', choices=trim_material_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_leakage_class = forms.ChoiceField(required=False, label= 'Leakage Class:', choices=leakage_class_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_fire_safe = forms.ChoiceField(required=False, label= 'Fire Safe:', choices=fire_safe_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	m_nace_requirement = forms.ChoiceField(required=False, label= 'Nace Requirement:', choices=nace_requirement_tuple, widget=forms.Select(attrs={
		'class': 'form-control',
		}))
	class Meta:
		model = Post
		fields = ['m_valve_type', 'm_body_size', 'm_body_material', 'm_rating', 'm_end_connections',
			'm_stem_material', 'm_seat_material', 'm_bonnet_bolting_material', 'm_trim_type',
			'm_trim_size', 'm_trim_material', 'm_leakage_class', 'm_fire_safe', 'm_nace_requirement',]