import 'package:flutter/material.dart';

import '../../core/destinations.dart';
import '../../shared/placeholder_tab.dart';

/// Class 6: routes + stops on flutter_map (static GTFS).
/// Class 9: live vehicle positions via the Cloud Function proxy.
class BusScreen extends StatelessWidget {
  const BusScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const PlaceholderTab(tab: AppTab.bus);
  }
}
