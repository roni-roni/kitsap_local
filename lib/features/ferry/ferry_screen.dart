import 'package:flutter/material.dart';

import '../../core/destinations.dart';
import '../../shared/placeholder_tab.dart';

/// Class 3: terminal list + next departures on MOCK data.
/// Class 6: swap the mock for the WSDOT API, add caching and error states.
class FerryScreen extends StatelessWidget {
  const FerryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const PlaceholderTab(tab: AppTab.ferry);
  }
}
