import java.util.*;
import java.util.concurrent.*;

class Worker implements Runnable {
    private final String name;
    private final String clan;

    public Worker(String name, String clan) {
        this.name = name;
        this.clan = clan;
    }

    @Override
    public void run() {
        Random rand = new Random();
        int taskCount = rand.nextInt(5) + 1;

        for (int i = 1; i <= taskCount; i++) {
            System.out.println(name + " from " + clan + " is processing task " + i);
            try {
                Thread.sleep(rand.nextInt(1000) + 500); // Simulate processing time
            } catch (InterruptedException e) {
                System.out.println(name + " was interrupted.");
            }
        }

        System.out.println(name + " from " + clan + " has completed all tasks.");
    }
}

public class ThreadClanManager {
    public static void main(String[] args) {
        // Clan grouping map
        Map<String, List<Worker>> clanMap = new HashMap<>();
        clanMap.put("Clan A", new ArrayList<>());
        clanMap.put("Clan B", new ArrayList<>());
        clanMap.put("Clan C", new ArrayList<>());

        // Assign workers to clans
        for (int i = 1; i <= 10; i++) {
            String name = "Worker" + i;
            String clan = switch (i % 3) {
                case 0 -> "Clan C";
                case 1 -> "Clan A";
                default -> "Clan B";
            };
            clanMap.get(clan).add(new Worker(name, clan));
        }

        // Run all workers using ExecutorService
        ExecutorService executor = Executors.newFixedThreadPool(10);
        for (var clanEntry : clanMap.entrySet()) {
            for (Worker worker : clanEntry.getValue()) {
                executor.submit(worker);
            }
        }

        executor.shutdown();
    }
}