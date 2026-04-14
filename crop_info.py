# crop_info.py

class CropInformation:
    def __init__(self):
        self.crop_details = {
            'rice': {
                'season': 'Kharif (June-November)',
                'duration': '120-150 days',
                'water_requirement': 'High (150-300 mm monthly)',
                'soil_type': 'Clayey loam, silt loam',
                'ideal_temp': '20-27°C',
                'ideal_ph': '5.5-7.0',
                'fertilizer': {'N': '80-120 kg/ha', 'P': '40-60 kg/ha', 'K': '40-60 kg/ha'},
                'tips': [
                    'Maintain 2-5 cm standing water during growing season',
                    'Transplant 21-25 day old seedlings',
                    'Apply nitrogen in 3 splits',
                    'Control weeds within first 30 days'
                ],
                'common_pests': ['Stem borer', 'Brown planthopper', 'Leaf folder'],
                'harvest_time': 'When 80% of grains turn golden yellow',
                'expected_yield': '4-6 tons/hectare'
            },
            'wheat': {
                'season': 'Rabi (November-April)',
                'duration': '120-150 days',
                'water_requirement': 'Moderate (50-100 mm monthly)',
                'soil_type': 'Loamy soil, well-drained',
                'ideal_temp': '15-25°C',
                'ideal_ph': '6.0-7.5',
                'fertilizer': {'N': '120-150 kg/ha', 'P': '60-80 kg/ha', 'K': '40-60 kg/ha'},
                'tips': [
                    'Sow at optimal moisture condition',
                    'First irrigation at 20-25 days (CRI stage)',
                    'Apply nitrogen in 2-3 splits',
                    'Maintain proper plant spacing'
                ],
                'common_pests': ['Aphids', 'Termites', 'Pink borer'],
                'harvest_time': 'When grains are hard and straw turns yellow',
                'expected_yield': '4-5 tons/hectare'
            },
            'maize': {
                'season': 'Kharif & Rabi',
                'duration': '80-120 days',
                'water_requirement': 'Moderate (60-110 mm monthly)',
                'soil_type': 'Well-drained loamy soil',
                'ideal_temp': '18-27°C',
                'ideal_ph': '5.5-7.0',
                'fertilizer': {'N': '120-150 kg/ha', 'P': '60-80 kg/ha', 'K': '40-60 kg/ha'},
                'tips': [
                    'Ensure proper drainage',
                    'Critical irrigation at tasseling stage',
                    'Control weeds in first 30-40 days',
                    'Maintain plant population of 60,000-75,000/ha'
                ],
                'common_pests': ['Stem borer', 'Fall armyworm', 'Shoot fly'],
                'harvest_time': 'When kernels are hard and moisture is 20-25%',
                'expected_yield': '5-7 tons/hectare'
            },
            'cotton': {
                'season': 'Kharif (April-December)',
                'duration': '150-180 days',
                'water_requirement': 'Moderate (60-120 mm monthly)',
                'soil_type': 'Deep black cotton soil',
                'ideal_temp': '21-30°C',
                'ideal_ph': '6.0-7.5',
                'fertilizer': {'N': '100-150 kg/ha', 'P': '50-70 kg/ha', 'K': '50-70 kg/ha'},
                'tips': [
                    'Grow Bt cotton varieties',
                    'First picking at 120 days',
                    'Monitor for pink bollworm regularly',
                    'Maintain proper plant spacing'
                ],
                'common_pests': ['Bollworm', 'Aphids', 'Whitefly'],
                'harvest_time': 'When bolls burst (3-4 pickings)',
                'expected_yield': '15-20 quintals/hectare'
            },
            'chickpea': {
                'season': 'Rabi (October-March)',
                'duration': '100-120 days',
                'water_requirement': 'Low (40-80 mm monthly)',
                'soil_type': 'Well-drained loamy soil',
                'ideal_temp': '15-25°C',
                'ideal_ph': '6.0-7.5',
                'fertilizer': {'N': '20-30 kg/ha', 'P': '50-60 kg/ha', 'K': '20-30 kg/ha'},
                'tips': [
                    'Treat seeds with Rhizobium culture',
                    'One irrigation at flowering stage',
                    'Avoid waterlogging',
                    'Can be grown as catch crop'
                ],
                'common_pests': ['Pod borer', 'Aphids', 'Cut worm'],
                'harvest_time': 'When 90% pods turn brown',
                'expected_yield': '15-20 quintals/hectare'
            },
            'kidneybeans': {
                'season': 'Kharif',
                'duration': '90-120 days',
                'water_requirement': 'Moderate',
                'soil_type': 'Well-drained loamy soil',
                'ideal_temp': '20-25°C',
                'ideal_ph': '6.0-7.0',
                'fertilizer': {'N': '20-40 kg/ha', 'P': '40-60 kg/ha', 'K': '20-40 kg/ha'},
                'tips': [
                    'Requires good drainage',
                    'Sensitive to waterlogging',
                    'Apply phosphorus at sowing',
                    'Support with stakes if needed'
                ],
                'common_pests': ['Pod borer', 'Aphids', 'Bean fly'],
                'harvest_time': 'When pods turn yellow-brown',
                'expected_yield': '15-18 quintals/hectare'
            },
            'pigeonpeas': {
                'season': 'Kharif',
                'duration': '150-180 days',
                'water_requirement': 'Low to Moderate',
                'soil_type': 'Well-drained soil',
                'ideal_temp': '20-30°C',
                'ideal_ph': '6.0-7.5',
                'fertilizer': {'N': '20-30 kg/ha', 'P': '40-50 kg/ha', 'K': '20-30 kg/ha'},
                'tips': [
                    'Drought tolerant crop',
                    'Good for intercropping',
                    'Improves soil fertility',
                    'Requires minimal irrigation'
                ],
                'common_pests': ['Pod borer', 'Pod fly', 'Plume moth'],
                'harvest_time': 'When pods turn brown',
                'expected_yield': '10-15 quintals/hectare'
            },
            'mothbeans': {
                'season': 'Kharif',
                'duration': '75-90 days',
                'water_requirement': 'Very Low',
                'soil_type': 'Sandy to loamy soil',
                'ideal_temp': '25-35°C',
                'ideal_ph': '6.5-8.0',
                'fertilizer': {'N': '15-20 kg/ha', 'P': '30-40 kg/ha', 'K': '15-20 kg/ha'},
                'tips': [
                    'Highly drought resistant',
                    'Suitable for arid regions',
                    'Minimal input requirement',
                    'Good for dryland farming'
                ],
                'common_pests': ['Aphids', 'Jassids'],
                'harvest_time': 'When pods mature',
                'expected_yield': '6-8 quintals/hectare'
            },
            'mungbean': {
                'season': 'Kharif & Summer',
                'duration': '60-75 days',
                'water_requirement': 'Moderate',
                'soil_type': 'Loamy to sandy loam',
                'ideal_temp': '25-35°C',
                'ideal_ph': '6.5-7.5',
                'fertilizer': {'N': '15-20 kg/ha', 'P': '40-50 kg/ha', 'K': '20-30 kg/ha'},
                'tips': [
                    'Short duration crop',
                    'Can be grown between two crops',
                    'Tolerates high temperature',
                    'Requires good drainage'
                ],
                'common_pests': ['Pod borer', 'Aphids', 'Whitefly'],
                'harvest_time': 'When 80% pods turn black',
                'expected_yield': '8-12 quintals/hectare'
            },
            'blackgram': {
                'season': 'Kharif & Rabi',
                'duration': '75-90 days',
                'water_requirement': 'Moderate',
                'soil_type': 'Loamy soil',
                'ideal_temp': '25-35°C',
                'ideal_ph': '6.5-7.5',
                'fertilizer': {'N': '20-25 kg/ha', 'P': '40-50 kg/ha', 'K': '20-30 kg/ha'},
                'tips': [
                    'Tolerates slight salinity',
                    'Responds well to phosphorus',
                    'Can be grown as catch crop',
                    'Requires 2-3 irrigations'
                ],
                'common_pests': ['Pod borer', 'Aphids', 'Jassids'],
                'harvest_time': 'When pods turn black',
                'expected_yield': '8-10 quintals/hectare'
            },
            'lentil': {
                'season': 'Rabi',
                'duration': '110-130 days',
                'water_requirement': 'Low',
                'soil_type': 'Well-drained loamy soil',
                'ideal_temp': '18-25°C',
                'ideal_ph': '6.0-8.0',
                'fertilizer': {'N': '15-20 kg/ha', 'P': '40-50 kg/ha', 'K': '20-25 kg/ha'},
                'tips': [
                    'Sensitive to waterlogging',
                    'Requires good drainage',
                    'One irrigation at flowering',
                    'Treat seeds with Rhizobium'
                ],
                'common_pests': ['Aphids', 'Pod borer', 'Bruchids'],
                'harvest_time': 'When plants turn yellow-brown',
                'expected_yield': '10-15 quintals/hectare'
            },
            'pomegranate': {
                'season': 'Year-round (Perennial)',
                'duration': '6-7 months per crop cycle',
                'water_requirement': 'Moderate',
                'soil_type': 'Well-drained loamy to sandy soil',
                'ideal_temp': '15-35°C',
                'ideal_ph': '6.5-7.5',
                'fertilizer': {'N': '200-300 kg/ha/year', 'P': '100-150 kg/ha/year', 'K': '150-200 kg/ha/year'},
                'tips': [
                    'Regular pruning required',
                    'Drip irrigation recommended',
                    'Mulching helps retain moisture',
                    'Fruit bagging prevents pest damage'
                ],
                'common_pests': ['Fruit borer', 'Aphids', 'Thrips'],
                'harvest_time': '5-6 months after flowering',
                'expected_yield': '15-20 tons/hectare'
            },
            'banana': {
                'season': 'Year-round (Perennial)',
                'duration': '11-15 months',
                'water_requirement': 'High',
                'soil_type': 'Deep, rich loamy soil',
                'ideal_temp': '15-35°C',
                'ideal_ph': '6.0-7.5',
                'fertilizer': {'N': '200-300 kg/ha', 'P': '60-100 kg/ha', 'K': '300-400 kg/ha'},
                'tips': [
                    'Requires regular irrigation',
                    'Mulching is beneficial',
                    'Remove suckers regularly',
                    'Protect from strong winds'
                ],
                'common_pests': ['Banana weevil', 'Aphids', 'Nematodes'],
                'harvest_time': 'When fingers are well filled',
                'expected_yield': '40-50 tons/hectare'
            },
            'mango': {
                'season': 'Year-round (Perennial)',
                'duration': 'Fruits after 3-4 years',
                'water_requirement': 'Moderate',
                'soil_type': 'Well-drained deep soil',
                'ideal_temp': '24-30°C',
                'ideal_ph': '5.5-7.5',
                'fertilizer': {'N': '100-150 kg/tree/year', 'P': '50-75 kg/tree/year', 'K': '100-125 kg/tree/year'},
                'tips': [
                    'Regular pruning needed',
                    'Irrigation during fruit development',
                    'Mulching beneficial',
                    'Protect from pests during flowering'
                ],
                'common_pests': ['Fruit fly', 'Mango hopper', 'Mealy bug'],
                'harvest_time': 'May-July (varies by variety)',
                'expected_yield': '10-15 tons/hectare'
            },
            'grapes': {
                'season': 'Year-round (Perennial)',
                'duration': '140-150 days per crop',
                'water_requirement': 'Moderate',
                'soil_type': 'Well-drained sandy loam',
                'ideal_temp': '15-35°C',
                'ideal_ph': '6.5-8.0',
                'fertilizer': {'N': '100-150 kg/ha', 'P': '50-100 kg/ha', 'K': '100-150 kg/ha'},
                'tips': [
                    'Requires trellising',
                    'Regular pruning essential',
                    'Drip irrigation recommended',
                    'Bunch thinning for quality'
                ],
                'common_pests': ['Downy mildew', 'Powdery mildew', 'Thrips'],
                'harvest_time': 'When sugar content reaches desired level',
                'expected_yield': '20-30 tons/hectare'
            },
            'watermelon': {
                'season': 'Summer',
                'duration': '80-90 days',
                'water_requirement': 'Moderate to High',
                'soil_type': 'Sandy loam with good drainage',
                'ideal_temp': '25-30°C',
                'ideal_ph': '6.0-7.0',
                'fertilizer': {'N': '100-120 kg/ha', 'P': '50-60 kg/ha', 'K': '80-100 kg/ha'},
                'tips': [
                    'Requires warm weather',
                    'Mulching helps conserve moisture',
                    'Avoid overhead irrigation',
                    'Harvest when tendril dries'
                ],
                'common_pests': ['Fruit fly', 'Aphids', 'Red pumpkin beetle'],
                'harvest_time': 'When underside turns yellow',
                'expected_yield': '25-35 tons/hectare'
            },
            'muskmelon': {
                'season': 'Summer',
                'duration': '75-90 days',
                'water_requirement': 'Moderate',
                'soil_type': 'Sandy loam',
                'ideal_temp': '25-30°C',
                'ideal_ph': '6.0-6.8',
                'fertilizer': {'N': '100-120 kg/ha', 'P': '50-60 kg/ha', 'K': '75-100 kg/ha'},
                'tips': [
                    'Needs warm, dry weather',
                    'Reduce irrigation near harvest',
                    'Mulching recommended',
                    'Hand pollination may be needed'
                ],
                'common_pests': ['Fruit fly', 'Aphids', 'Downy mildew'],
                'harvest_time': 'When fruits slip easily from vine',
                'expected_yield': '15-20 tons/hectare'
            },
            'apple': {
                'season': 'Temperate (Perennial)',
                'duration': 'Fruits after 4-5 years',
                'water_requirement': 'Moderate',
                'soil_type': 'Well-drained loamy soil',
                'ideal_temp': '15-25°C',
                'ideal_ph': '5.5-6.5',
                'fertilizer': {'N': '200-400 kg/ha', 'P': '100-200 kg/ha', 'K': '200-300 kg/ha'},
                'tips': [
                    'Requires chilling hours',
                    'Regular pruning essential',
                    'Thinning for quality fruits',
                    'Protect from late frosts'
                ],
                'common_pests': ['Codling moth', 'Aphids', 'Scab'],
                'harvest_time': 'September-November',
                'expected_yield': '15-25 tons/hectare'
            },
            'orange': {
                'season': 'Year-round (Perennial)',
                'duration': 'Fruits after 3-4 years',
                'water_requirement': 'Moderate to High',
                'soil_type': 'Well-drained loamy soil',
                'ideal_temp': '15-30°C',
                'ideal_ph': '6.0-7.5',
                'fertilizer': {'N': '200-300 kg/ha', 'P': '100-150 kg/ha', 'K': '150-200 kg/ha'},
                'tips': [
                    'Regular irrigation needed',
                    'Mulching beneficial',
                    'Prune dead/diseased branches',
                    'Protect from citrus pests'
                ],
                'common_pests': ['Citrus psylla', 'Leaf miner', 'Fruit fly'],
                'harvest_time': 'November-March',
                'expected_yield': '20-30 tons/hectare'
            },
            'papaya': {
                'season': 'Year-round',
                'duration': '10-12 months',
                'water_requirement': 'High',
                'soil_type': 'Well-drained sandy loam',
                'ideal_temp': '22-28°C',
                'ideal_ph': '6.0-7.0',
                'fertilizer': {'N': '200-250 kg/ha', 'P': '100-150 kg/ha', 'K': '200-250 kg/ha'},
                'tips': [
                    'Requires good drainage',
                    'Sensitive to waterlogging',
                    'Remove male plants after identification',
                    'Protect from strong winds'
                ],
                'common_pests': ['Fruit fly', 'Aphids', 'Mites'],
                'harvest_time': 'When fruit shows yellow color',
                'expected_yield': '50-80 tons/hectare'
            },
            'coconut': {
                'season': 'Year-round (Perennial)',
                'duration': 'Fruits after 5-6 years',
                'water_requirement': 'High',
                'soil_type': 'Sandy loam to laterite',
                'ideal_temp': '27-32°C',
                'ideal_ph': '5.5-8.0',
                'fertilizer': {'N': '100-150 kg/palm/year', 'P': '50-100 kg/palm/year', 'K': '150-200 kg/palm/year'},
                'tips': [
                    'Requires coastal conditions',
                    'Regular irrigation essential',
                    'Mulching with coconut husks',
                    'Remove dead/diseased fronds'
                ],
                'common_pests': ['Red palm weevil', 'Rhinoceros beetle', 'Mites'],
                'harvest_time': 'Year-round (every 45 days)',
                'expected_yield': '80-100 nuts/palm/year'
            },
            'jute': {
                'season': 'Kharif',
                'duration': '120-150 days',
                'water_requirement': 'High',
                'soil_type': 'Alluvial loamy soil',
                'ideal_temp': '25-35°C',
                'ideal_ph': '6.0-7.5',
                'fertilizer': {'N': '60-80 kg/ha', 'P': '30-40 kg/ha', 'K': '30-40 kg/ha'},
                'tips': [
                    'Requires high humidity',
                    'Needs frequent irrigation',
                    'Harvest when flowering starts',
                    'Retting for 15-20 days'
                ],
                'common_pests': ['Stem weevil', 'Semilooper', 'Hairy caterpillar'],
                'harvest_time': 'When flowering begins',
                'expected_yield': '20-25 quintals/hectare (fiber)'
            },
            'coffee': {
                'season': 'Year-round (Perennial)',
                'duration': 'Fruits after 3-4 years',
                'water_requirement': 'Moderate to High',
                'soil_type': 'Well-drained loamy soil',
                'ideal_temp': '15-28°C',
                'ideal_ph': '6.0-6.5',
                'fertilizer': {'N': '200-300 kg/ha', 'P': '100-150 kg/ha', 'K': '150-250 kg/ha'},
                'tips': [
                    'Requires shade trees',
                    'Mulching essential',
                    'Proper spacing important',
                    'Regular pruning needed'
                ],
                'common_pests': ['Coffee berry borer', 'Leaf miner', 'White stem borer'],
                'harvest_time': 'December-February',
                'expected_yield': '1000-1500 kg/hectare (clean coffee)'
            }
        }

    def get_crop_info(self, crop_name):
        """Get detailed information about a crop"""
        # Convert to lowercase for matching
        crop_key = crop_name.lower()
        return self.crop_details.get(crop_key, None)

    def get_all_crops(self):
        """Get list of all available crops"""
        return [crop.title() for crop in self.crop_details.keys()]

    def get_crop_summary(self, crop_name):
        """Get brief summary of a crop"""
        info = self.get_crop_info(crop_name)
        if info:
            return f"{crop_name.title()} - {info['season']} | Duration: {info['duration']} | Yield: {info['expected_yield']}"
        return None


# Test
if __name__ == "__main__":
    crop_info = CropInformation()

    print("=" * 60)
    print("CROP INFORMATION DATABASE")
    print("=" * 60)

    print(f"\nTotal Crops: {len(crop_info.get_all_crops())}")
    print("\nAvailable Crops:")
    for i, crop in enumerate(crop_info.get_all_crops(), 1):
        print(f"{i:2}. {crop}")

    # Test with rice
    print("\n" + "=" * 60)
    print("SAMPLE: RICE INFORMATION")
    print("=" * 60)

    rice = crop_info.get_crop_info('rice')
    if rice:
        print(f"\n📅 Season: {rice['season']}")
        print(f"⏱️  Duration: {rice['duration']}")
        print(f"💧 Water: {rice['water_requirement']}")
        print(f"🌡️  Temperature: {rice['ideal_temp']}")
        print(f"🌾 Yield: {rice['expected_yield']}")