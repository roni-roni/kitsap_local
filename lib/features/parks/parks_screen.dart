import 'package:flutter/material.dart';

import '../../core/destinations.dart';
import '../../shared/placeholder_tab.dart';

/// Class 3: park list on MOCK data. Class 4: filters (owner, Discover Pass).
/// Class 6: real locations and boundaries from county / state datasets.
class ParksScreen extends StatelessWidget {
  const ParksScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const PlaceholderTab(tab: AppTab.parks);
  }
}
