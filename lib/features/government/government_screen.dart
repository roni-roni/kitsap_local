import 'package:flutter/material.dart';

import '../../core/destinations.dart';
import '../../shared/placeholder_tab.dart';

/// Class 5: county officials (from tools/county_officials.py) + meetings.
/// Class 9: "report an issue" hand-off to SeeClickFix and county forms.
class GovernmentScreen extends StatelessWidget {
  const GovernmentScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const PlaceholderTab(tab: AppTab.government);
  }
}
